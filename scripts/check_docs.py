"""Validate relative Markdown links in contributor-facing documentation."""
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
FILES = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "CODE_OF_CONDUCT.md", ROOT / "TODO.md"]
FILES += sorted((ROOT / "docs").rglob("*.md"))
FILES += sorted((ROOT / "research").rglob("*.md"))
FILES += sorted((ROOT / "skills").rglob("*.md"))
pattern = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
checked = 0

for document in FILES:
    for raw in pattern.findall(document.read_text()):
        target = raw.strip().split(maxsplit=1)[0].strip("<>")
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        path_text = unquote(target.split("#", 1)[0])
        if not path_text:
            continue
        destination = (document.parent / path_text).resolve()
        assert destination == ROOT or ROOT in destination.parents, f"Link escapes repository: {document}: {target}"
        assert destination.exists(), f"Broken documentation link: {document.relative_to(ROOT)} -> {target}"
        checked += 1

print(f"PASS: {checked} relative documentation links resolve across {len(FILES)} Markdown files")
