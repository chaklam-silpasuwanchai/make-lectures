---
name: make-workshop-doc
description: Writes and revises hands-on workshop handouts (lab docs that go with a lecture) the way Dr. Chaklam wants them - plain English, real files to upload, copy-ready prompts, follow-up prompts that push the first answer, and a visual wherever one helps - and works through his doc comments one by one. Use for "rewrite my workshop handout", "make a workshop doc", "turn this into labs", "handle my comments on the workshop doc", or /make-workshop-doc.
---

# Make a Workshop Doc

A workshop doc is what people keep open on their laptop while they do the labs. They follow it step by step, copy the prompts, and come back to it on Monday. It has to be easy to follow without the teacher in the room.

## 1. Start from his material
- Read his original handout and the lab files in full, including the pictures in it. Keep his own screenshots and infographics; they are part of the teaching.
- Keep his labs, files and order. Fix what is wrong (old model names, wrong acronyms, notes-to-self) and say what you fixed.
- Make it a Claude Doc (the docs connector) unless he names another format.

## 2. Use the standard shape
`references/format.md` has the section order and the lab format. In short: a one-line lead, "Before you start", where this fits in the series, the tools and words they need, the prompt pattern, the labs, what we learned, homework, resources.

## 3. Follow the rules
Read `references/rules.md` before writing and before handing over. The slide rules in `../make-lecture-deck/references/rules.md` (plain English, explain every term and number, delete the obvious, search what changes) apply here too; this skill's file holds only what is special to docs.

## 4. Check before handing over
- Look at every diagram and chart (a screenshot read): nothing clipped or overlapping, the title states the point and is true for every data point.
- Every number in a chart comes from the lab file it describes.
- One short line in chat with the link and what changed.

## 5. Work through his comments
Doc comments arrive as `[Artifact comment sent to Claude]`. For each: re-read that part of the doc, make the change (an `update` with `answering` set to the thread's root id), and reply under that root with the new wording. Don't use the artifact comment tool for docs, and don't resolve threads. A question means the doc is unclear: answer it and fix the doc. When a comment states a general preference, add it to `references/rules.md` with his words quoted, and apply it to the whole doc.
