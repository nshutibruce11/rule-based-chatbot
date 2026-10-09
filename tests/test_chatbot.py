import os
import sys
import unittest
from io import StringIO
from unittest.mock import patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import chatbot


def reply(text, memory=None):
    return chatbot.get_response(text, memory)[0]


class TestGreetingsAndExit(unittest.TestCase):
    def test_greetings_any_case_and_spaces(self):
        for text in ["hello", "HELLO", "HeLLo", "  hi  ", "Hey", "Hello!", "Good Morning"]:
            self.assertEqual(reply(text), "Hello! How can I help you today?", text)

    def test_exit_commands(self):
        for text in ["bye", "exit", "quit", "goodbye", " QUIT ", "BYE!"]:
            message, done = chatbot.get_response(text)
            self.assertTrue(done, text)
            self.assertIn("Goodbye", message)

    def test_greeting_does_not_exit(self):
        self.assertFalse(chatbot.get_response("hello")[1])


class TestKnowledgeBase(unittest.TestCase):
    def test_has_5_plus_intents(self):
        self.assertGreaterEqual(len(chatbot.KNOWLEDGE_BASE), 5)

    def test_known_inputs(self):
        self.assertIn("doing well", reply("How are you?"))
        self.assertIn("RuleBot", reply("what is your name"))
        self.assertIn("DecodeLabs", reply("Who made you?"))
        self.assertIn("human intelligence", reply("what is AI"))
        self.assertIn("Try:", reply("  HELP "))
        self.assertEqual(reply("Thanks!"), "You're welcome!")

    def test_extra_spaces_inside_message(self):
        self.assertIn("human intelligence", reply("what   is    ai"))


class TestSessionMemoryAndNestedLogic(unittest.TestCase):
    def test_remembers_name(self):
        memory = {}
        self.assertIn("Sam", reply("My name is sam", memory))
        self.assertEqual(reply("what is my name?", memory), "Your name is Sam.")
        self.assertEqual(reply("hello", memory), "Hello, Sam! How can I help you today?")
        self.assertIn("Sam", reply("bye", memory))

    def test_name_unknown_and_missing(self):
        self.assertIn("don't know", reply("what is my name", {}))
        self.assertIn("didn't catch", reply("my name is", {}))


class TestTimeAndDate(unittest.TestCase):
    def test_time_and_date(self):
        self.assertTrue(reply("what time is it?").startswith("It is "))
        self.assertTrue(reply("date").startswith("Today is "))


class TestFallbackAndEmpty(unittest.TestCase):
    def test_unknown_input(self):
        for text in ["xyz123", "Tell me something unknown."]:
            message, done = chatbot.get_response(text)
            self.assertIn("still learning", message)
            self.assertFalse(done)

    def test_empty_input(self):
        for text in ["", "   ", "\t"]:
            message, done = chatbot.get_response(text)
            self.assertIn("Please type", message)
            self.assertFalse(done)


class TestLoop(unittest.TestCase):
    def run_main(self, inputs):
        feed = iter(inputs)
        with patch("builtins.input", lambda _: next(feed)), \
             patch("sys.stdout", new=StringIO()) as out:
            chatbot.main()
        return out.getvalue(), feed

    def test_multi_message_session_stops_on_exit(self):
        text, feed = self.run_main(["hi", "how are you?", "xyz123", "", "quit", "NOT READ"])
        self.assertIn("Goodbye", text)
        self.assertEqual(next(feed), "NOT READ")  # loop stopped after quit

    def test_ends_cleanly_when_input_ends(self):
        def raise_eof(_):
            raise EOFError
        with patch("builtins.input", raise_eof), patch("sys.stdout", new=StringIO()) as out:
            chatbot.main()
        self.assertIn("Goodbye", out.getvalue())


if __name__ == "__main__":
    unittest.main()
