#!/usr/bin/env node
import { createReadStream } from "node:fs";
import { mkdir, readFile, readdir, stat, writeFile } from "node:fs/promises";
import { createServer } from "node:http";
import { dirname, extname, relative, resolve } from "node:path";
import { performance } from "node:perf_hooks";
import { pathToFileURL } from "node:url";


function fail(message) {
  throw new Error(message);
}

function parsePositiveInteger(value, label, { allowZero = false } = {}) {
  const parsed = Number(value);
  if (!Number.isSafeInteger(parsed) || parsed < (allowZero ? 0 : 1)) {
    fail(`${label} must be ${allowZero ? "a non-negative" : "a positive"} integer`);
  }
  return parsed;
}

function parseArguments(argv) {
  const positional = [];
  const options = {};
  for (let index = 0; index < argv.length; index += 1) {
    const value = argv[index];
    if (!value.startsWith("--")) {
      positional.push(value);
      continue;
    }
    const next = argv[index + 1];
    if (next === undefined || next.startsWith("--")) {
      fail(`${value} requires a value`);
    }
    options[value.slice(2)] = next;
    index += 1;
  }
  if (positional.length !== 3) {
    fail(
      "usage: benchmark-pagefind.mjs SITE_DIR QUERY_FIXTURE.json THRESHOLDS.json "
      + "--hugo-ms N --pagefind-ms N --prebenchmark-ms N --report FILE "
      + "[--cold-rounds N] [--warm-rounds N]"
    );
  }
  const allowedOptions = new Set([
    "hugo-ms",
    "pagefind-ms",
    "prebenchmark-ms",
    "report",
    "cold-rounds",
    "warm-rounds",
  ]);
  for (const option of Object.keys(options)) {
    if (!allowedOptions.has(option)) {
      fail(`unknown option --${option}`);
    }
  }
  for (const required of ["hugo-ms", "pagefind-ms", "prebenchmark-ms", "report"]) {
    if (!(required in options)) {
      fail(`missing --${required}`);
    }
  }
  return {
    siteDir: resolve(positional[0]),
    fixturePath: resolve(positional[1]),
    thresholdsPath: resolve(positional[2]),
    reportPath: resolve(options.report),
    hugoMs: parsePositiveInteger(options["hugo-ms"], "--hugo-ms", { allowZero: true }),
    pagefindMs: parsePositiveInteger(options["pagefind-ms"], "--pagefind-ms", { allowZero: true }),
    prebenchmarkMs: parsePositiveInteger(
      options["prebenchmark-ms"],
      "--prebenchmark-ms",
      { allowZero: true }
    ),
    warmRounds: parsePositiveInteger(options["warm-rounds"] ?? "5", "--warm-rounds"),
    coldRounds: parsePositiveInteger(options["cold-rounds"] ?? "3", "--cold-rounds"),
  };
}

function normalizeExpectedPath(value) {
  if (typeof value !== "string" || !value.startsWith("/")) {
    fail(`expected URL must be an absolute site path: ${JSON.stringify(value)}`);
  }
  const decoded = decodeURIComponent(new URL(value, "https://fixture.invalid").pathname);
  return decoded.endsWith("/") ? decoded : `${decoded}/`;
}

function normalizeActualPath(value) {
  if (typeof value !== "string" || value.length === 0) {
    return "";
  }
  const decoded = decodeURIComponent(new URL(value, "https://fixture.invalid").pathname);
  return decoded.endsWith("/") ? decoded : `${decoded}/`;
}

function validateQueries(payload) {
  if (!payload || payload.version !== 1 || !Array.isArray(payload.queries) || payload.queries.length === 0) {
    fail("query fixture must have version 1 and a non-empty queries array");
  }
  const ids = new Set();
  for (const item of payload.queries) {
    for (const field of ["id", "query", "expected_url", "expected_type", "expected_group"]) {
      if (typeof item[field] !== "string" || item[field].trim() === "") {
        fail(`query fixture ${JSON.stringify(item.id)} has invalid ${field}`);
      }
    }
    if (ids.has(item.id)) {
      fail(`duplicate query fixture id: ${item.id}`);
    }
    ids.add(item.id);
    normalizeExpectedPath(item.expected_url);
    for (const expected of item.also_expected_results ?? []) {
      for (const field of ["url", "type", "group"]) {
        if (typeof expected[field] !== "string" || expected[field].trim() === "") {
          fail(`query fixture ${item.id} has invalid also_expected_results.${field}`);
        }
      }
      normalizeExpectedPath(expected.url);
    }
  }
}

const REQUIRED_MINIMUMS = ["page_count", "pages_per_second", "recall_at_5", "mrr"];
const REQUIRED_MAXIMUMS = [
  "index_bytes",
  "hugo_ms",
  "pagefind_ms",
  "end_to_end_ms",
  "cold_query_p50_ms",
  "cold_query_p95_ms",
  "warm_query_p50_ms",
  "warm_query_p95_ms",
];

function validateThresholds(payload) {
  if (!payload || payload.version !== 1 || !payload.minimums || !payload.maximums) {
    fail("threshold fixture must have version 1, minimums, and maximums");
  }
  for (const [section, names] of [
    ["minimums", REQUIRED_MINIMUMS],
    ["maximums", REQUIRED_MAXIMUMS],
  ]) {
    for (const name of names) {
      const value = payload[section][name];
      if (typeof value !== "number" || !Number.isFinite(value) || value < 0) {
        fail(`threshold ${section}.${name} must be a non-negative finite number`);
      }
    }
  }
}

function contentType(path) {
  return {
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".wasm": "application/wasm",
  }[extname(path)] ?? "application/octet-stream";
}

async function startPagefindServer(pagefindDir) {
  const root = resolve(pagefindDir);
  const server = createServer(async (request, response) => {
    try {
      const url = new URL(request.url ?? "/", "http://127.0.0.1");
      if (!url.pathname.startsWith("/pagefind/")) {
        response.writeHead(404).end();
        return;
      }
      const requested = resolve(root, decodeURIComponent(url.pathname.slice("/pagefind/".length)));
      const rel = relative(root, requested);
      if (rel.startsWith("..") || rel === "" || resolve(root, rel) !== requested) {
        response.writeHead(403).end();
        return;
      }
      const fileStat = await stat(requested);
      if (!fileStat.isFile()) {
        response.writeHead(404).end();
        return;
      }
      response.writeHead(200, { "content-type": contentType(requested) });
      createReadStream(requested).pipe(response);
    } catch {
      response.writeHead(404).end();
    }
  });
  await new Promise((resolveListen, rejectListen) => {
    server.once("error", rejectListen);
    server.listen(0, "127.0.0.1", resolveListen);
  });
  const address = server.address();
  if (!address || typeof address === "string") {
    server.close();
    fail("could not bind the local Pagefind benchmark server");
  }
  return {
    basePath: `http://127.0.0.1:${address.port}/pagefind/`,
    close: () => new Promise((resolveClose, rejectClose) => {
      server.close((error) => error ? rejectClose(error) : resolveClose());
    }),
  };
}

async function directoryBytes(path) {
  let total = 0;
  for (const entry of await readdir(path, { withFileTypes: true })) {
    const child = resolve(path, entry.name);
    if (entry.isDirectory()) {
      total += await directoryBytes(child);
    } else if (entry.isFile()) {
      total += (await stat(child)).size;
    }
  }
  return total;
}

function percentile(values, fraction) {
  if (values.length === 0) {
    fail("cannot calculate a percentile without samples");
  }
  const sorted = [...values].sort((left, right) => left - right);
  const index = Math.max(0, Math.ceil(fraction * sorted.length) - 1);
  return sorted[index];
}

function rounded(value) {
  return Math.round(value * 1000) / 1000;
}

function expectedResults(item) {
  return [
    { url: item.expected_url, type: item.expected_type, group: item.expected_group },
    ...(item.also_expected_results ?? []),
  ];
}

function matchesExpected(data, expected) {
  return normalizeActualPath(data.url).endsWith(normalizeExpectedPath(expected.url))
    && data.meta?.type === expected.type
    && data.meta?.group === expected.group;
}

async function executeQuery(instance, item) {
  const options = item.filters ? { filters: item.filters } : {};
  const search = await instance.search(item.query, options);
  return Promise.all(search.results.slice(0, 5).map(async (result, index) => ({
    rank: index + 1,
    data: await result.data(),
  })));
}

async function destroy(instance) {
  if (typeof instance.destroy === "function") {
    await instance.destroy();
  }
}

function evaluateThresholds(metrics, thresholds) {
  const failures = [];
  for (const name of REQUIRED_MINIMUMS) {
    if (metrics[name] < thresholds.minimums[name]) {
      failures.push(`${name}=${metrics[name]} is below minimum ${thresholds.minimums[name]}`);
    }
  }
  for (const name of REQUIRED_MAXIMUMS) {
    if (metrics[name] > thresholds.maximums[name]) {
      failures.push(`${name}=${metrics[name]} exceeds maximum ${thresholds.maximums[name]}`);
    }
  }
  return failures;
}

async function main() {
  const benchmarkStarted = performance.now();
  const args = parseArguments(process.argv.slice(2));
  const pagefindDir = resolve(args.siteDir, "pagefind");
  const queriesPayload = JSON.parse(await readFile(args.fixturePath, "utf8"));
  const thresholds = JSON.parse(await readFile(args.thresholdsPath, "utf8"));
  validateQueries(queriesPayload);
  validateThresholds(thresholds);

  const entry = JSON.parse(await readFile(resolve(pagefindDir, "pagefind-entry.json"), "utf8"));
  if (typeof entry.version !== "string" || !entry.languages || typeof entry.languages !== "object") {
    fail("Pagefind entry metadata is malformed");
  }
  const pageCount = Object.values(entry.languages).reduce((total, language) => {
    if (!Number.isSafeInteger(language.page_count) || language.page_count < 0) {
      fail("Pagefind language page_count is malformed");
    }
    return total + language.page_count;
  }, 0);
  const indexBytes = await directoryBytes(pagefindDir);
  const modulePath = resolve(pagefindDir, "pagefind.js");
  const pagefindModule = await import(`${pathToFileURL(modulePath).href}?benchmark=${Date.now()}`);
  if (typeof pagefindModule.createInstance !== "function") {
    fail(`${modulePath} does not export createInstance()`);
  }

  const localServer = await startPagefindServer(pagefindDir);
  const createInstance = () => pagefindModule.createInstance({
    basePath: localServer.basePath,
    ranking: { metaWeights: { aliases: 10.0 } },
  });
  const coldLatencies = [];
  const warmLatencies = [];
  let foundExpected = 0;
  let expectedTotal = 0;
  let reciprocalRankTotal = 0;
  let warmInstance;
  try {
    for (let round = 0; round < args.coldRounds; round += 1) {
      for (const item of queriesPayload.queries) {
        const started = performance.now();
        const instance = createInstance();
        try {
          await instance.init();
          await executeQuery(instance, item);
        } finally {
          await destroy(instance);
        }
        coldLatencies.push(performance.now() - started);
      }
    }

    warmInstance = createInstance();
    await warmInstance.init();
    for (const item of queriesPayload.queries) {
      await executeQuery(warmInstance, item);
    }
    const qualityRows = new Map();
    for (let round = 0; round < args.warmRounds; round += 1) {
      for (const item of queriesPayload.queries) {
        const started = performance.now();
        const rows = await executeQuery(warmInstance, item);
        warmLatencies.push(performance.now() - started);
        if (round === 0) {
          qualityRows.set(item.id, rows);
        }
      }
    }
    for (const item of queriesPayload.queries) {
      const rows = qualityRows.get(item.id) ?? [];
      const expected = expectedResults(item);
      expectedTotal += expected.length;
      foundExpected += expected.filter((target) => rows.some(({ data }) => matchesExpected(data, target))).length;
      const primary = rows.find(({ data }) => matchesExpected(data, expected[0]));
      reciprocalRankTotal += primary ? 1 / primary.rank : 0;
    }
  } finally {
    if (warmInstance) {
      await destroy(warmInstance);
    }
    await localServer.close();
  }

  const benchmarkMs = Math.ceil(performance.now() - benchmarkStarted);
  const endToEndMs = args.prebenchmarkMs + benchmarkMs;
  const metrics = {
    page_count: pageCount,
    index_bytes: indexBytes,
    hugo_ms: args.hugoMs,
    pagefind_ms: args.pagefindMs,
    prebenchmark_pipeline_ms: args.prebenchmarkMs,
    benchmark_ms: benchmarkMs,
    end_to_end_ms: endToEndMs,
    pages_per_second: endToEndMs === 0 ? 0 : rounded(pageCount / (endToEndMs / 1000)),
    cold_query_p50_ms: rounded(percentile(coldLatencies, 0.5)),
    cold_query_p95_ms: rounded(percentile(coldLatencies, 0.95)),
    warm_query_p50_ms: rounded(percentile(warmLatencies, 0.5)),
    warm_query_p95_ms: rounded(percentile(warmLatencies, 0.95)),
    recall_at_5: rounded(foundExpected / expectedTotal),
    mrr: rounded(reciprocalRankTotal / queriesPayload.queries.length),
  };
  const thresholdFailures = evaluateThresholds(metrics, thresholds);
  const report = {
    version: 1,
    pagefind_version: entry.version,
    methodology: {
      timing_clock: "Node.js performance.now monotonic clock",
      cold_query: "new Pagefind instance; init plus query plus top-five data load",
      warm_query: "initialized instance after one full fixture warm-up; query plus top-five data load",
      percentile: "nearest-rank",
      recall_at_5: "expected result items found in the top five divided by all expected result items",
      mrr: "mean reciprocal rank of each fixture's primary expected result within the top five",
      end_to_end: "projection, Hugo, Pagefind, semantic checks, fixture checks, and this benchmark",
    },
    fixture: relative(process.cwd(), args.fixturePath),
    thresholds: relative(process.cwd(), args.thresholdsPath),
    samples: {
      queries: queriesPayload.queries.length,
      expected_results: expectedTotal,
      cold_queries: coldLatencies.length,
      cold_rounds: args.coldRounds,
      warm_queries: warmLatencies.length,
      warm_rounds: args.warmRounds,
    },
    metrics,
    threshold_failures: thresholdFailures,
  };
  await mkdir(dirname(args.reportPath), { recursive: true });
  await writeFile(args.reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
  console.log(JSON.stringify(report, null, 2));
  if (thresholdFailures.length > 0) {
    for (const failure of thresholdFailures) {
      console.error(`ERROR: ${failure}`);
    }
    process.exitCode = 1;
  }
}

main().catch((error) => {
  console.error(`ERROR: ${error.message}`);
  process.exitCode = 1;
});
