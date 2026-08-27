#!/usr/bin/env bash
set -euo pipefail

root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
fixture="${root}/tests/fixtures/pagefind_same_name"
temp_dir=$(mktemp -d)
cleanup() {
  rm -rf "${temp_dir}"
}
trap cleanup EXIT INT TERM

site_dir="${temp_dir}/site"
mkdir -p "${site_dir}/layouts/partials"
cp -R "${fixture}/." "${site_dir}/"
cp "${root}/layouts/partials/search-aliases.html" \
  "${site_dir}/layouts/partials/search-aliases.html"

hugo build \
  --source "${site_dir}" \
  --destination "${temp_dir}/public" \
  --cleanDestinationDir \
  --minify
"${root}/node_modules/.bin/pagefind" --site "${temp_dir}/public"
node "${root}/scripts/verify-pagefind-queries.mjs" \
  "${temp_dir}/public" \
  "${fixture}/queries.json"
