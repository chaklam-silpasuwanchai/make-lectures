# make-lectures (v0.1.0)

Skills for making teaching materials the way Chaklam wants them: plain English, low reading load, big visuals, a source on every claim, real cases, and a hands-on activity. Lecture decks now; workshop docs next.

## Install

In Claude Code:

```
/plugin marketplace add chaklam-silpasuwanchai/make-lectures
/plugin install teach@make-lectures
```

In the Claude app, you can also save a skill directly from a chat or upload its folder.

## Skills

| Skill | What it does | Say |
|---|---|---|
| `make-lecture-deck` | Builds and revises a lecture or workshop slide deck, and works through your slide comments one by one. | "make a lecture on …", "redesign my slides", "handle my comments on the deck" |
| *(next)* workshop doc | A hands-on workshop handout to go with a lecture. | |

## How it learns

Each rule in `plugins/teach/skills/make-lecture-deck/references/rules.md` comes from a real comment, quoted next to it. When a new comment states a general preference, the skill offers to add it there, so you only have to say it once.

## Layout

```
plugins/teach/skills/make-lecture-deck/
  SKILL.md                  the steps
  references/rules.md       slide rules, each with the comment that taught it
  references/cases.md       how to pick interesting case studies
  references/comments.md    how to work through slide comments
  references/genai-content.md  content decisions from the GenAI lecture
```
