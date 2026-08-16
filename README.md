# JUMP OS

An AI-operated lead generation system for Jump Web Design. This repo is
not just files: it is an operating system that any AI coding agent
(Claude Code, Codex, Cursor, or similar) can open and run. The agent
reads the instructions inside, becomes the operator, and a single
sentence like "scrape all of Washington" is a complete command: it sets
up the scraper, runs for hours autonomously, verifies everything, and
files the results as calling-ready lead lists.

## The fastest way to understand it

Open this folder with an AI agent and say:

> **give me a tour**

It will walk you through the whole system with live numbers and answer
any question. No agent handy? Start with these two files:

- [`STATE.md`](STATE.md) — where everything stands right now
- [`02-LEADS/REPORT.md`](02-LEADS/REPORT.md) — the live scoreboard:
  every niche, county, batch, and its calling status

## What's inside

```
01-PLAYBOOK/               the craft: call scripts, call records, training
02-LEADS/                  the product: Teleblast-ready CSVs by niche,
                           class, state, and county, plus the tracker
                           and the generated report
03-LEAD-SOURCING-ENGINE/   the machinery: two acquisition engines and
                           SHIPPING, the only path leads take into
                           02-LEADS (its registry makes double-calling
                           structurally impossible)
04-SKILLS/                 trigger-phrase instructions for AI operators
                           (the tour lives here)
99-ARCHIVE/                frozen history, read-only
AGENTS.md                  the constitution: laws, layout, boot order
STATE.md                   the single answer to "where are we"
```

## How leads are organized

`02-LEADS/<NICHE>/<CLASS>/<STATE>/<NN-COUNTY>/` where Class A means no
usable website (best prospects), Class B means a website with real
flaws. Every county folder has `00-MASTER` (the full list) and
`BATCHES` (files of at most 100 leads, best first, which is what gets
loaded into the dialer). County folders are numbered by lead count.

Every lead appears exactly once, is verified in-territory, and is
recorded in a permanent registry so no business is ever exported or
called twice.

## Operating it

Read [`AGENTS.md`](AGENTS.md) first, then
[`03-LEAD-SOURCING-ENGINE/README.md`](03-LEAD-SOURCING-ENGINE/README.md).
Running on a new machine: [`03-LEAD-SOURCING-ENGINE/SETUP.md`](03-LEAD-SOURCING-ENGINE/SETUP.md).
