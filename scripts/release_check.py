"""Fail CI when required production metadata, routes, or native assets regress."""
import json
import struct
from pathlib import Path

root = Path(__file__).resolve().parents[1]
public = root / "public"
mobile = root / "apps/mobile"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def png_size(path):
    with path.open("rb") as image:
        require(image.read(8) == b"\x89PNG\r\n\x1a\n", f"Not a PNG: {path}")
        length = struct.unpack(">I", image.read(4))[0]
        require(image.read(4) == b"IHDR" and length >= 8, f"Missing PNG header: {path}")
        return struct.unpack(">II", image.read(8))


config = json.loads((mobile / "app.json").read_text())["expo"]
require(config["scheme"] == "islamiclives", "Stable custom URL scheme is required")
require(config["ios"]["bundleIdentifier"] == "build.ummah.islamiclives", "Stable iOS ID required")
require(config["android"]["package"] == "build.ummah.islamiclives", "Stable Android ID required")
for key in ("icon",):
    asset = mobile / config[key]
    require(asset.exists() and png_size(asset) == (1024, 1024), f"{key} must be a 1024px PNG")
for asset_name in (config["splash"]["image"], config["android"]["adaptiveIcon"]["foregroundImage"]):
    require((mobile / asset_name).exists(), f"Missing native asset: {asset_name}")

required_routes = ["index.html", "404.html", "about/index.html", "explore/index.html",
                   "people/index.html", "prophets/index.html", "scholars/index.html", "spread/index.html"]
for route in required_routes:
    require((public / route).exists(), f"Missing crawlable route: {route}")

html_files = list(public.glob("**/*.html"))
indexable_files = [page for page in html_files if page.name != "404.html"]
for page in indexable_files:
    html = page.read_text()
    for marker in ('<title>', 'name="description"', 'rel="canonical"', 'property="og:title"',
                   'name="twitter:title"', 'application/ld+json', 'data-site-footer'):
        require(marker in html, f"Missing {marker} in {page.relative_to(root)}")
require('name="robots" content="noindex"' in (public / "404.html").read_text(), "404 must be noindex")

social_image = public / "og.png"
require(social_image.exists() and png_size(social_image) == (1200, 630), "Social preview must be a 1200×630 PNG")
preview_pages = [public / route for route in ("index.html", "about/index.html", "explore/index.html",
                                              "people/index.html", "prophets/index.html",
                                              "scholars/index.html", "spread/index.html")]
for page in preview_pages:
    html = page.read_text()
    for marker in ('property="og:image"', 'property="og:image:alt"',
                   'name="twitter:card" content="summary_large_image"', 'name="twitter:image"'):
        require(marker in html, f"Missing social preview metadata in {page.relative_to(root)}")
for page in list((public / "people").glob("*/index.html")) + list((public / "prophets").glob("*/index.html")):
    profile_html = page.read_text()
    require('property="og:image"' not in profile_html, f"Generic image must not imply a person portrait: {page.relative_to(root)}")
    require('class="fact-grid"' in profile_html and profile_html.count("<dt>") == 4,
            f"Static profile facts must survive JavaScript failure: {page.relative_to(root)}")

robots = (public / "robots.txt").read_text()
sitemap = (public / "sitemap.xml").read_text()
require("Sitemap:" in robots and "<urlset" in sitemap, "Search discovery files are incomplete")
require((public / "llms.txt").stat().st_size > 300, "llms.txt is unexpectedly empty")

mobile_source = (mobile / "App.js").read_text()
require("AsyncStorage" in mobile_source and "SAVED_KEY" in mobile_source, "Saved profiles must persist")
require("Alert.alert" in mobile_source, "External failures need a user-visible state")
web_source = (public / "app.js").read_text()
require("localStorage" in web_source and "savedDirectory" in web_source, "Web saved profiles must persist and remain browsable")

print(f"PASS: release contract; {len(indexable_files)} metadata-complete indexable pages; native IDs and artwork.")
