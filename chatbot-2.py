"""RuleBot - Rule-Based AI Chatbot (DecodeLabs AI Project 1).

Input -> Process -> Output (IPO model):
  INPUT    read the message and sanitize it (case, spaces, punctuation)
  PROCESS  explicit if / elif / else decisions + a dictionary knowledge base
  OUTPUT   print the reply, then loop again until the user exits

No external libraries are needed. Python 3 only.
"""

from datetime import datetime

BOT_NAME = "RuleBot"

GREETINGS = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
EXIT_COMMANDS = ["bye", "exit", "quit", "goodbye"]
TIME_QUESTIONS = ["time", "what time is it", "what is the time", "what's the time"]
DATE_QUESTIONS = ["date", "what is the date", "what is today's date", "what day is it"]

# Knowledge base: a dictionary of intents (key = user message, value = reply).
KNOWLEDGE_BASE = {
    "how are you": "I am doing well, thank you! How are you?",
    "i am fine": "Glad to hear that! What would you like to talk about?",
    "i am good": "Glad to hear that! What would you like to talk about?",
    "what is your name": "I'm " + BOT_NAME + ", a rule-based chatbot.",
    "who made you": "I was built as a DecodeLabs Project 1 exercise.",
    "what can you do": "I greet you, answer simple questions, tell the time and date, "
                       "remember your name, and say goodbye. Type 'help' for ideas.",
    "what is ai": "AI is software that performs tasks that normally need human intelligence.",
    "what is a rule based chatbot": "It answers using fixed if/else rules written by a "
                                    "programmer, instead of learning from data.",
    "what is python": "Python is a beginner-friendly programming language, "
                      "and it is what I am written in.",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
    "help": "Try: hello, how are you, what is your name, what is ai, what time is it, "
            "my name is <name>, tell me a joke, or bye.",
}

FALLBACK_REPLY = "I am still learning! I don't understand that message yet. Type 'help' to see what I know."


def sanitize(raw_text):
    """INPUT stage: lowercase, remove extra spaces and ending punctuation."""
    text = raw_text.lower().strip()
    text = text.strip("?!.,").strip()
    text = " ".join(text.split())  # "what   is  ai" -> "what is ai"
    return text


def get_response(raw_text, memory=None):
    """PROCESS stage: choose a reply with if/elif/else.

    memory is a dict that stores facts during one session (for example the
    user's name). Returns (reply, should_exit).
    """
    if memory is None:
        memory = {}
    message = sanitize(raw_text)

    if message == "":
        return "Please type something so I can help.", False

    elif message in EXIT_COMMANDS:
        if memory.get("name"):  # nested condition: personalise the goodbye
            return "Goodbye, " + memory["name"] + "! Thank you for chatting with me.", True
        return "Goodbye! Thank you for chatting with me.", True

    elif message in GREETINGS:
        if memory.get("name"):
            return "Hello, " + memory["name"] + "! How can I help you today?", False
        return "Hello! How can I help you today?", False

    elif message.startswith("my name is"):
        name = message[len("my name is"):].strip()
        if name == "":
            return "I didn't catch your name. Try: my name is Sam", False
        memory["name"] = name.title()
        return "Nice to meet you, " + memory["name"] + "!", False

    elif message in ("what is my name", "who am i"):
        if memory.get("name"):
            return "Your name is " + memory["name"] + ".", False
        return "I don't know your name yet. Tell me: my name is <name>", False

    elif message in TIME_QUESTIONS:
        return "It is " + datetime.now().strftime("%I:%M %p") + ".", False

    elif message in DATE_QUESTIONS:
        return "Today is " + datetime.now().strftime("%A, %d %B %Y") + ".", False

    else:
        # Dictionary lookup with a built-in fallback for unknown messages
        return KNOWLEDGE_BASE.get(message, FALLBACK_REPLY), False


def main():
    """OUTPUT stage and the continuous loop."""
    memory = {}
    print("Welcome! I am your rule-based AI chatbot. Type 'bye' to exit.")
    while True:  # continuous loop
        try:
            user_text = input("You: ")
        except (EOFError, KeyboardInterrupt):  # input ended or Ctrl+C
            print("\nChatbot: Goodbye! Thank you for chatting with me.")
            break
        reply, should_exit = get_response(user_text, memory)
        print("Chatbot:", reply)
        if should_exit:
            break  # clean exit


if __name__ == "__main__":
    main()
