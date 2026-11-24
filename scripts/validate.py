#!/usr/bin/env python3
"""Validate the make-lectures repo. Run: python scripts/validate.py  (needs: pip install pyyaml)"""
import json, re, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Install PyYAML first: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins" / "teach" / "skills"
errors = []

names = []
for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    f = d / "SKILL.md"
    if not f.exists():
        errors.append(f"{d.name}: SKILL.md missing"); continue
    text = f.read_text()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{d.name}: no frontmatter"); continue
    fm = yaml.safe_load(m.group(1))
    names.append(d.name)
    if fm.get("name") != d.name: errors.append(f"{d.name}: name '{fm.get('name')}' != folder")
    if not re.fullmatch(r"[a-z]+(-[a-z]+)*", d.name): errors.append(f"{d.name}: use lowercase hyphenated words")
    desc = fm.get("description", "")
    if not desc or len(desc) > 1024: errors.append(f"{d.name}: description missing or over 1024 chars")
    for ref in re.findall(r"references/[\w\-]+\.md", text):
        if not (d / ref).exists(): errors.append(f"{d.name}: mentions missing file {ref}")

readme = (ROOT / "README.md").read_text()
for n in names:
    if f"`{n}`" not in readme: errors.append(f"README.md does not list `{n}`")

pv = json.loads((ROOT / "plugins/teach/.claude-plugin/plugin.json").read_text())["version"]
mv = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["plugins"][0]["version"]
cl = re.search(r"^## (\d+\.\d+\.\d+)", (ROOT / "CHANGELOG.md").read_text(), re.M)
rv = re.search(r"\(v(\d+\.\d+\.\d+)\)", readme)
found = {"plugin": pv, "marketplace": mv, "changelog": cl and cl.group(1), "README title": rv and rv.group(1)}
if len(set(found.values())) != 1:
    errors.append("version mismatch: " + ", ".join(f"{k} {v}" for k, v in found.items()))

for e in errors: print("ERROR:", e)
if not errors: print(f"{len(names)} skill(s) checked, version {pv}")
sys.exit(1 if errors else 0)
