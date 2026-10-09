# Submission Checklist

## Requirements
- [ ] Handles greetings and exit commands
- [ ] Uses if / elif / else logic
- [ ] Runs in a continuous `while` loop and stops cleanly with `break`
- [ ] Sanitizes case and whitespace
- [ ] Dictionary knowledge base with 5+ intents
- [ ] Fallback reply for unknown input

## Verification (tick only after you checked it yourself)
- [ ] `python -m unittest discover -v tests` shows OK
- [ ] Manual checks done on my own device: hello / HELLO / HeLLo, How are you?, xyz123, empty Enter, bye, quit
- [ ] Ran it on my phone in Pydroid 3 and took a screenshot

## Files
- [ ] chatbot.py, README.md, DEMO.md, tests/test_chatbot.py

## Understanding
- [ ] I can explain why the loop stops after `bye`
- [ ] I can explain why `sanitize()` is needed
- [ ] I can add a new intent to the dictionary

## Before sending
- [ ] Read DecodeLabs' submission instructions (platform, deadline, format); I did not see them in the PDF screenshots
