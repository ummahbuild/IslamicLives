"""A deterministic 100-point production contract: 81 profiles + 19 app invariants."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
data = json.loads((PUBLIC / "data/people.json").read_text())
people = data["people"]
passed = []

for person in people:
    sources = person.get("sources", [])
    chapters = person.get("chapters", [])
    ok = all([
        person.get("id"), person.get("name"), person.get("arabic"),
        person.get("category"), person.get("role"), person.get("date"),
        person.get("place"), person.get("uncertainty"), sources, chapters,
        all(source.get("url", "").startswith("https://") and source.get("kind") for source in sources),
        all(chapter.get("text") and chapter.get("sources") for chapter in chapters),
    ])
    assert ok, f"Profile production contract failed: {person.get('id')}"
    passed.append(f"profile:{person['id']}")

ids = {person["id"] for person in people}
web = (PUBLIC / "app.js").read_text()
style = (PUBLIC / "style.css").read_text()
mobile = (ROOT / "apps/mobile/App.js").read_text()
atlas = json.loads((PUBLIC / "data/atlas.json").read_text())
profile_pages = list((PUBLIC / "people").glob("*/index.html")) + list((PUBLIC / "prophets").glob("*/index.html"))

global_checks = [
    (len(people) == 81, "collection count"),
    (len(ids) == len(people), "unique profile IDs"),
    (sum(person["category"] == "Prophets" for person in people) == 25, "prophet count"),
    (len({person["category"] for person in people}) >= 5, "category coverage"),
    (len({source["kind"] for person in people for source in person["sources"]}) >= 4 and all("Surah " in source["title"] for person in people for source in person["sources"] if "quran.com/" in source["url"]), "evidence classes and named-surah citations"),
    (len(profile_pages) == 81 and all((PUBLIC / "spread" / event["id"] / "index.html").exists() for event in atlas["events"]), "generated profile and atlas routes"),
    (all('class="fact-grid"' in page.read_text() for page in profile_pages), "static fact cards"),
    ("journey-person" in web and "Currently exploring" in web and "hasPlottableYear(p.year)" in web, "prominent journey identity and evidence-gated time chart"),
    ("journey-person-select" in web and "Change person" in web, "journey person selector"),
    ("aria-label',`Currently exploring" in web, "journey identity accessible name"),
    (".journey-person" in style and "@media(max-width:650px)" in style, "responsive journey identity"),
    ("function JourneyPerson" in mobile and "CURRENTLY EXPLORING" in mobile, "native journey identity"),
    ('accessibilityRole="progressbar"' in mobile, "native journey progress semantics"),
    ("localStorage" in web and "AsyncStorage" in mobile, "saved-life persistence parity"),
    (len(atlas["events"]) == 16 and len(atlas["regions"]) == 6, "atlas chapter and region contract"),
    (all(token in (PUBLIC / "atlas.js").read_text() for token in ['value="0.5"', 'value="1"', 'value="2"', 'id="atlas-status"', 'cumulativeAtlasContext(data,index)']), "atlas playback, announcements, and cumulative context"),
    ((ROOT / "CONTRIBUTING.md").exists() and (ROOT / "TODO.md").exists(), "contributor documentation"),
    ((ROOT / ".github/PULL_REQUEST_TEMPLATE.md").exists() and (ROOT / ".github/ISSUE_TEMPLATE/content-correction.yml").exists(), "GitHub contributor templates"),
    ((ROOT / ".github/workflows/ci.yml").exists() and "npm run ci" in (ROOT / ".github/workflows/ci.yml").read_text(), "hosted CI contract"),
]

for condition, label in global_checks:
    assert condition, f"Production contract failed: {label}"
    passed.append(label)

assert len(passed) == 100, f"Expected exactly 100 production points, got {len(passed)}"
print("PASS: 100/100 production points (81 profile contracts + 19 product, accessibility, parity, documentation, and CI invariants)")
