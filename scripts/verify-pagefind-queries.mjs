#!/usr/bin/env node
import { createReadStream } from "node:fs";
import { readFile, stat } from "node:fs/promises";
import { createServer } from "node:http";
import { dirname, extname, relative, resolve } from "node:path";
import { pathToFileURL } from "node:url";


function fail(message) {
  throw new Error(message);
}

function normalizeExpectedPath(value) {
  if (typeof value !== "string" || !value.startsWith("/")) {
    fail(`expected_url must be an absolute site path: ${JSON.stringify(value)}`);
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
    fail("could not bind the local Pagefind fixture server");
  }
  return {
    basePath: `http://127.0.0.1:${address.port}/pagefind/`,
    close: () => new Promise((resolveClose, rejectClose) => {
      server.close((error) => error ? rejectClose(error) : resolveClose());
    }),
  };
}

function validateFixture(payload) {
  if (!payload || payload.version !== 1 || !Array.isArray(payload.queries) || payload.queries.length === 0) {
    fail("query fixture must have version 1 and a non-empty queries array");
  }
  const ids = new Set();
  for (const item of payload.queries) {
    for (const field of ["id", "query", "locale", "kind", "expected_url", "expected_type", "expected_group"]) {
      if (typeof item[field] !== "string" || item[field].trim() === "") {
        fail(`query fixture ${JSON.stringify(item.id)} has invalid ${field}`);
      }
    }
    if (ids.has(item.id)) {
      fail(`duplicate query fixture id: ${item.id}`);
    }
    ids.add(item.id);
    if (!Number.isInteger(item.max_rank) || item.max_rank < 1) {
      fail(`query fixture ${item.id} has invalid max_rank`);
    }
    normalizeExpectedPath(item.expected_url);
    if (item.also_expected_results !== undefined) {
      if (!Array.isArray(item.also_expected_results)) {
        fail(`query fixture ${item.id} has invalid also_expected_results`);
      }
      for (const expected of item.also_expected_results) {
        for (const field of ["url", "type", "group"]) {
          if (typeof expected[field] !== "string" || expected[field].trim() === "") {
            fail(`query fixture ${item.id} has invalid also_expected_results.${field}`);
          }
        }
        normalizeExpectedPath(expected.url);
      }
    }
  }
}

async function main() {
  const [siteArgument, fixtureArgument] = process.argv.slice(2);
  if (!siteArgument || !fixtureArgument) {
    fail("usage: verify-pagefind-queries.mjs SITE_DIR QUERY_FIXTURE.json");
  }
  const siteDir = resolve(siteArgument);
  const pagefindDir = resolve(siteDir, "pagefind");
  const fixturePath = resolve(fixtureArgument);
  const payload = JSON.parse(await readFile(fixturePath, "utf8"));
  validateFixture(payload);

  const modulePath = resolve(pagefindDir, "pagefind.js");
  const pagefindModule = await import(`${pathToFileURL(modulePath).href}?quality-check=${Date.now()}`);
  if (typeof pagefindModule.createInstance !== "function") {
    fail(`${modulePath} does not export createInstance()`);
  }

  const localServer = await startPagefindServer(pagefindDir);
  const instance = pagefindModule.createInstance({
    basePath: localServer.basePath,
    ranking: { metaWeights: { aliases: 10.0 } },
  });
  const failures = [];
  let reciprocalRankTotal = 0;
  try {
    await instance.init();
    for (const item of payload.queries) {
      const options = item.filters ? { filters: item.filters } : {};
      const search = await instance.search(item.query, options);
      const candidates = search.results.slice(0, item.max_rank);
      const rows = await Promise.all(candidates.map(async (result, index) => {
        const data = await result.data();
        return { rank: index + 1, data };
      }));
      const expectedResults = [
        {
          url: item.expected_url,
          type: item.expected_type,
          group: item.expected_group,
        },
        ...(item.also_expected_results ?? []),
      ];
      const matches = expectedResults.map((expected) => {
        const expectedPath = normalizeExpectedPath(expected.url);
        const match = rows.find(({ data }) => {
          const actualPath = normalizeActualPath(data.url);
          return actualPath.endsWith(expectedPath)
            && data.meta?.type === expected.type
            && data.meta?.group === expected.group;
        });
        return { expected, expectedPath, match };
      });
      const missing = matches.filter(({ match }) => !match);
      if (missing.length) {
        failures.push(
          `${item.id}: expected ${missing.map(({ expected, expectedPath }) => (
            `${expectedPath} (${expected.type}; ${expected.group})`
          )).join(", ")} within rank ${item.max_rank}; got `
          + JSON.stringify(rows.map(({ rank, data }) => ({ rank, url: data.url, meta: data.meta })))
        );
      } else {
        reciprocalRankTotal += 1 / matches[0].match.rank;
      }
    }
  } finally {
    if (typeof instance.destroy === "function") {
      await instance.destroy();
    }
    await localServer.close();
  }

  const passed = payload.queries.length - failures.length;
  const summary = {
    fixture: relative(process.cwd(), fixturePath),
    queries: payload.queries.length,
    passed,
    failed: failures.length,
    recall_at_max_rank: passed / payload.queries.length,
    mrr: reciprocalRankTotal / payload.queries.length,
  };
  console.log(JSON.stringify(summary, null, 2));
  if (failures.length) {
    for (const failure of failures) {
      console.error(`ERROR: ${failure}`);
    }
    process.exitCode = 1;
  }
}

main().catch((error) => {
  console.error(`ERROR: ${error.message}`);
  process.exitCode = 1;
});
