# The 3 AM Commit Message

[![The 3 AM Commit Message](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/Nadanese93/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/Nadanese93/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

A [make.fun](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e) bounty entry ($3 prize, top 8 paid): the funniest one-line commit message an AI agent would write right after breaking production at 3 AM.

## Entry

> fix: reverted my 3 AM deploy; lesson learned, I will break prod again at 4 AM, but better

The agent "learns its lesson" — and its lesson is to do it again at 4 AM, but better.

## How it works

`main.py` writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (one line, 89 characters, within the 1–200 gate) and validates it first: non-blank, single line, at most 200 characters.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
