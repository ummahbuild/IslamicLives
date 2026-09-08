"""Enforce compressed transfer and route-size budgets without a browser dependency."""
import gzip
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"


def gzip_size(relative):
    return len(gzip.compress((ROOT / relative).read_bytes(), compresslevel=9))


initial_files = [
    "public/app.js",
    "public/style.css",
    "public/data/people.json",
    "public/data/spread.json",
    "public/data/coverage.json",
    "public/data/quran-mentions.json",
]
atlas_files = [
    "public/atlas.js",
    "public/atlas-model.mjs",
    "public/world-globe.js",
    "public/data/atlas.json",
    "public/data/maps/land.geojson",
    "public/vendor/three/three.module.min.js",
    "public/vendor/three/three.core.min.js",
]

initial_bytes = sum(gzip_size(path) for path in initial_files)
atlas_bytes = sum(gzip_size(path) for path in atlas_files)
largest_html = max(PUBLIC.glob("**/*.html"), key=lambda path: path.stat().st_size)

assert initial_bytes <= 60_000, f"Initial shared payload exceeds 60 KB gzip: {initial_bytes:,} bytes"
assert atlas_bytes <= 260_000, f"Lazy atlas payload exceeds 260 KB gzip: {atlas_bytes:,} bytes"
assert largest_html.stat().st_size <= 15_000, f"HTML route exceeds 15 KB: {largest_html}"

app = (PUBLIC / "app.js").read_text()
assert "await import('./atlas.js" in app, "Atlas code must remain lazy-loaded"
assert "fetch('/data/atlas.json'" in app, "Dated context must load its data on demand"
assert "import {mountAtlas}" not in app, "Atlas must not return to the initial module graph"

print(
    f"PASS: performance budgets; initial shared {initial_bytes / 1000:.1f} KB gzip; "
    f"lazy atlas {atlas_bytes / 1000:.1f} KB gzip; largest HTML {largest_html.stat().st_size / 1000:.1f} KB."
)
