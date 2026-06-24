# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Initially the app looked good on the surface, but as i started to test it and use different inputs i began to encounter quit a few bugs.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
* Reveresed hint messages - When you insert a valuse that is higher than the HINT value it says "GO HIGHER" while when you Insert a value that is less than the HINT value it says "GO LOWER" (Error found in the check guess function lines 106-112)

*Attempts start at 1: When the app begins it already says you had one attempt and lessons the attempt left from 8 to 7.

* difficulty change doesn't reset secret: changing difficulty changes the range you can guess from eg. 1-50, but keeps the old secret (which can be out of range).
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret 50, guess 70 | Hint: go lower | Hint: "Go HIGHER!" | UI shows "📈 Go HIGHER!" warning |
| Fresh Normal game | 8 attempts left | 7 attempts left | None |
| Empty guess + Submit | Error, no attempt used | Error, attempt still increments | "Enter a guess." |
| Guess too high on attempt 2 | Score decreases or stays same | Score increases by 5 | None |
| Switch Easy after Normal secret=87 | New secret in 1–20 | Secret stays 87 | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
The AI i used is Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). one example of what the AI suggested was that the check guess fucntion was incorrect. i then went the the app.py code and located the error and ticked it off in my documentation as an error and restructured the function. thus fixing the error.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I submitted an empty guess and lost an attempt, the AI blamed `parse_guess` in `logic_utils.py`. I read the code and saw it already rejects empty input correctly. Testing again with Developer Debug Info open showed attempts still incrementing, so the real bug was in `app.py` — `attempts += 1` runs before validation.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed when two things were both true: the pytest test I wrote for it passed, and I could reproduce the original scenario in the live game and see the correct behavior. The tests gave me confidence the logic was right; the live game confirmed the UI wired it up correctly.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
For the hint bug, I wrote a test asserting that `check_guess(60, 40)` returns `"Too High"`, then confirmed in the running app that a guess of 60 against a secret of 40 now shows "Go LOWER!" instead of "Go HIGHER!". The pytest result verified the core logic in `logic_utils.py`; the manual check in Streamlit showed the fix actually reached the player-facing UI.

- Did AI help you design or understand any tests? How?
AI helped me structure the pytest file by suggesting which edge cases to cover, though I had to correct one test that used the wrong expected return value for `parse_guess`. That correction was important because it reminded me to verify AI-generated test expectations against the actual function behavior, not just accept them as correct.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the entire Python script from top to bottom every time the user interacts with the page — clicking a button, typing in a box, anything. Without session state, every rerun would reset all your variables and the game would forget everything. Session state is like a sticky note on the side of a whiteboard that never gets erased — you put things there that need to survive between reruns, like attempts, score, and the secret number. I would tell a friend: "Imagine your script is a whiteboard that gets wiped clean every second. Session state is the sticky note where you write down what you need to remember."

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to keep doing what i did here — write down bugs in a table first, then fix them one at a time and check each fix with both pytest and the running app. That combo stopped me from thinking something was fixed when only half the problem was solved.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time i would read through the relevant code myself before asking AI for a fix, especially for bugs that span more than one file. AI pointed me at `parse_guess` when the real issue was in `app.py`, and i lost time chasing the wrong function.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
AI is a good starting point for finding bugs and writing tests, but i don't trust it blindly anymore. I treat its suggestions like hints — i still have to read the code and test it myself before calling something done. I now realize the importance of using Ai as a tool and not a result or solution giver.

---
