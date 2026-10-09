# RuleBot - Rule-Based AI Chatbot
DecodeLabs Artificial Intelligence, Project 1 (Industrial Training Kit, Batch 2026)

## Overview
RuleBot is a terminal chatbot that answers using explicit `if / elif / else`
rules and a dictionary knowledge base. It runs in a continuous loop until the
user types an exit command. It is **rule-based AI**: every reply was written by
a programmer, nothing is learned from data, so behaviour is predictable and
easy to explain (a "white box").

## Objectives (from the assignment)
- Handle greetings and exit commands
- Use if-else logic for responses
- Run in a continuous loop
- Demonstrate control flow, decision-making logic and basic AI concepts

## How it matches the "Logic Skeleton" checklist
| Item | Where in `chatbot.py` |
|---|---|
| Input loop (continuous `while`) | `main()` -> `while True` |
| Sanitization (case and whitespace) | `sanitize()` |
| Knowledge base: dictionary, 5+ intents | `KNOWLEDGE_BASE` (13 entries) |
| Fallback for unknowns | `KNOWLEDGE_BASE.get(message, FALLBACK_REPLY)` |
| Exit strategy: clean `break` | `if should_exit: break` |

## Architecture (IPO model)
1. **Input**: `input()` then `sanitize()` (lowercase, trim spaces, remove ending punctuation)
2. **Process**: `get_response()` decides with `if / elif / else`; unknown text goes to the dictionary `.get()` fallback
3. **Output**: print the reply and repeat until exit

## Features
- Greetings: hello, hi, hey, good morning/afternoon/evening
- Exit: bye, exit, quit, goodbye
- Case-insensitive, ignores extra spaces and ending punctuation (`  HOW ARE YOU?  ` works)
- Dictionary knowledge base (AI, Python, jokes, thanks, help and more)
- Remembers your name during a session (`my name is Sam`), with nested conditions
- Tells the time and date (Python standard library)
- Handles empty input, Ctrl+C and ended input without crashing
- Friendly, consistent personality

## Requirements
Python 3. No external libraries, internet, database or API key.

## Run
Computer: `python chatbot.py` (or `python3 chatbot.py`)
Android: install Pydroid 3, open `chatbot.py`, tap the yellow Run button.

## Example
See `DEMO.md` for a full session. Short version:

    Welcome! I am your rule-based AI chatbot. Type 'bye' to exit.
    You: Hello
    Chatbot: Hello! How can I help you today?
    You: xyz123
    Chatbot: I am still learning! I don't understand that message yet. Type 'help' to see what I know.
    You: bye
    Chatbot: Goodbye! Thank you for chatting with me.

## Testing
Automated (13 tests): `python -m unittest discover -v tests`
Manual: run the program and try `hello`, `HELLO`, `HeLLo`, `How are you?`, `xyz123`, an empty Enter, `bye`, and `quit`.

## Rule-based AI vs machine learning
Rule-based: a human writes the rules, replies are fixed and fully traceable.
Machine learning: a model learns patterns from data, replies are probabilistic.

## Limitations
- Exact matching only: rephrased sentences ("how's it going") are not understood
- Memory lasts only for one session
- It does not learn from conversations
