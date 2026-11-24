# Working on the make-lectures repo

This repo holds the `teach` plugin: skills for making teaching materials (lecture decks now, workshop docs next).

## Every change
1. **Bump the version** in `plugins/teach/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, and the README title. PATCH for wording or a new rule, MINOR for a new skill or changed behavior.
2. Add a `CHANGELOG.md` entry under the new version.
3. Run `python scripts/validate.py` (needs `pyyaml`); it must pass.
4. Commit, push, open a pull request, and merge it.

## Skill rules
- Skill names: lowercase hyphenated words starting with a verb (`make-lecture-deck`).
- Keep each `SKILL.md` lean; put detail in its `references/`.
- A new rule from Chaklam's feedback goes in `make-lecture-deck/references/rules.md`, with his comment quoted next to it. One rule, one home: other files point to it, never copy it.
- A new skill also goes in the README table.
