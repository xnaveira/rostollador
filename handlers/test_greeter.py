from telegram.ext import MessageHandler
from handlers import greeter
import unittest
from unittest.mock import Mock
import re
import yaml


class TestGreeter(unittest.TestCase):

    def test_greeter1(self):
        with open('handlers/greeters.yml') as f:
            gs = f.read()
        update = Mock()
        update.effective_user.first_name = 'Xavier'
        for g in yaml.full_load_all(gs):
            rx = re.compile(g.regex)
            expected = []
            for pc in g.regex_positive_tests:
                self.assertIsNotNone(rx.search(pc))
            for nc in g.regex_negative_tests:
                self.assertIsNone(rx.search(nc))
            for greeting in g.greetings:
                expected.append(greeting.format(update.effective_user.first_name))
            i = 0
            while i < len(g.greetings) * 10:
                i = i + 1
                self.assertTrue(g._build_answer(update) in expected)
            isinstance(g.get_handler(), MessageHandler)


if __name__ == '__main__':
    unittest.main()