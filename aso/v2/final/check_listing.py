"""Check listing-text.md: field limits, and keywords match more-locales.md / README.md."""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
LIMITS = {"Promotional Text": 170, "Description": 4000}

text = (HERE / "listing-text.md").read_text(encoding="utf-8")
published = (HERE / "more-locales.md").read_text(encoding="utf-8") + (HERE.parent / "README.md").read_text(encoding="utf-8")
banned = {"1rm", "5x5", "531", "fitness", "health", "sport", "sports"}

errors = 0
for section in re.split(r"^## ", text, flags=re.M)[2:]:
    locale = section.splitlines()[0].strip()
    for field, body in re.findall(r"\*\*(.+?)\*\*\n```\n(.*?)\n```", section, flags=re.S):
        size, nbytes = len(body), len(body.encode())
        note = ""
        if field == "Keywords":
            words = body.split(",")
            bad = [w for w in words if w in banned or w != w.strip() or not w]
            dupes = {w for w in words if words.count(w) > 1}
            ok = nbytes <= 100 and not bad and not dupes and f"`{body}`" in published
            if f"`{body}`" not in published:
                note += " not the published pick"
            if bad or dupes:
                note += f" bad words {bad + sorted(dupes)}"
            limit = "100 bytes"
        else:
            ok = size <= LIMITS[field]
            limit = LIMITS[field]
        errors += not ok
        print(f"{'ok ' if ok else 'BAD'} {locale:20} {field:17} {size:5} chars {nbytes:5} bytes (limit {limit}){note}")

sys.exit(1 if errors else 0)
