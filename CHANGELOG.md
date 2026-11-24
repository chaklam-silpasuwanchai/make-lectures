# Changelog

**Every update bumps the version** (MINOR = a new skill or changed behavior; PATCH = wording or a new rule). Change it in `plugins/teach/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, and the README title. `scripts/validate.py` checks they match.

## 0.1.0
- **New skill `make-lecture-deck`:** builds and revises lecture and workshop decks the way Chaklam wants them, and works through his slide comments one by one. References: `rules.md` (slide rules, each with the comment that taught it), `cases.md` (picking interesting case studies), `comments.md` (the comment workflow), `genai-content.md` (content decisions from "Generative AI: The Big Picture", AIT, Nov 2026).
