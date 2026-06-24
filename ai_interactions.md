# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the agent to add two stretch features to my Streamlit number-guessing game in a single request:

1. **Guess History Sidebar Chart** — a bar chart in the sidebar showing every valid guess in the current game, with bar height equal to the guess value and a horizontal reference line at the secret number. Only show the chart after at least one valid guess.
2. **Persistent High Score** — `load_high_score(filepath)` and `save_high_score(filepath, score)` in `logic_utils.py`, load the high score at startup, compare on win, save if it is a new record, and display the current high score in the sidebar.

I also asked for `# FEATURE: [what this does]` comments above each new block and to leave all existing bug fixes untouched.

**What did the agent do?**

The agent read `app.py`, `logic_utils.py`, and `tests/test_game_logic.py`, then made these changes:

| File | Changes |
|------|---------|
| `logic_utils.py` | Added `load_high_score()` (returns `0` if the file is missing or unreadable) and `save_high_score()` (writes an integer to a plain text file). |
| `app.py` | Imported matplotlib and the new helpers; added `HIGH_SCORE_FILE = "high_score.txt"`; loaded high score into `st.session_state` at startup; displayed it with `st.sidebar.metric`; built a matplotlib bar chart in the sidebar filtered to valid integer guesses only, with a red dashed `axhline` at the secret number; on win, compared final score to the record and called `save_high_score` when beaten. |
| `requirements.txt` | Added `matplotlib` after I hit a `ModuleNotFoundError` on first run. |

Later in the same session I asked the agent to add pytest cases for the new functions. It added five tests to `tests/test_game_logic.py` using pytest's `tmp_path` fixture so tests never touch the real `high_score.txt`.

Commands the agent ran: `python3 -m pytest tests/ -v` (16 tests passed) and `pip3 install matplotlib`.

**What did you have to verify or fix manually?**

- **Missing dependency** — The first `streamlit run` failed with `ModuleNotFoundError: No module named 'matplotlib'`. The agent had used `matplotlib.pyplot` for the reference line but had not added it to `requirements.txt` until I reported the error. After `pip3 install matplotlib` and restarting Streamlit, the app ran correctly.
- **Chart only for valid guesses** — I confirmed invalid entries (e.g. `"abc"`) stay in `history` for debugging but do not appear as bars; only `isinstance(g, int)` values are charted.
- **High score persistence** — I won a game, checked that `high_score.txt` was created/updated in the project root, refreshed the app, and confirmed the sidebar still showed the saved record.
- **Bug fixes preserved** — I skimmed the diff to make sure existing `FIX:` comments (attempts starting at 0, reversed hints, win score formula) were not changed.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| File does not exist | "Add pytest cases for the new functions" | `test_load_high_score_missing_file` — `load_high_score(tmp_path / "missing.txt") == 0` | Yes | Matches the spec: return 0 when there is no file. `tmp_path` avoids touching real `high_score.txt`. |
| Valid file with integer | Same prompt | `test_load_high_score_valid_file` — write `"85"`, assert load returns `85` | Yes | Confirms normal read path and that `.strip()` handles trailing newlines. |
| File with non-integer content | Same prompt | `test_load_high_score_invalid_content` — write `"not-a-number"`, assert `0` | Yes | Covers the `ValueError` branch in `load_high_score` without crashing. |
| Save writes correct value | Same prompt | `test_save_high_score` — save `120`, assert file text is `"120"` | Yes | Verifies plain-text integer write with no extra formatting. |
| Round-trip save then load | Same prompt | `test_save_and_load_high_score` — save `40`, load back `40` | Yes | End-to-end check that the two functions work together like the app does on win. |

**How I ran the tests:**

```bash
python3 -m pytest tests/ -v
```

All 16 tests pass (11 original + 5 new high-score tests).

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

*Not attempted for this stretch feature work.*

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

*Not attempted for this stretch feature work.*
