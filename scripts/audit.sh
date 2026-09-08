#!/bin/sh
set -eu
python3 scripts/build_data.py
python3 scripts/build_pages.py
python3 scripts/sync_content.py
python3 scripts/validate.py
python3 scripts/check_internal_links.py
python3 scripts/test_mentions.py
node --check public/app.js
node --test scripts/test_atlas.mjs scripts/test_population_chart.mjs
