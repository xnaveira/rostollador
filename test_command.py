import re
from unittest.mock import Mock
import greeter

import command
import unittest


class TestCommand(unittest.TestCase):

    def test_version(self):
        version = '1.2.3'
        c = command.Command(
            'versio',
            'La meva versió és {}',
            [version],
            None
        )
        self.assertEqual(c._build_answer(), 'La meva versió és 1.2.3')


class TestGreeter(unittest.TestCase):

    def greeter1(self):
        rx = re.compile('.*[H|h]ola.*')
        rx_tests = [
            'Hola nois',
            'hola tiu',
            'no dius hola?',
            'holahola',
        ]
        update = Mock()
        update.effective_user.first_name = 'Xavier'
        greetings = ['Hola {}', 'Què tal {}?', 'Com vas {}?', 'Què dius {}?', 'Com ho portes {}?']
        for case in rx_tests:
            self.assertIsNotNone(rx.search(case))
        expected = []
        for g in greetings:
            expected.append(g.format(update.effective_user.first_name))
        g = greeter.Greeter(
            greetings,
            None,
            100
        )
        i = 0
        while i < len(greetings) * 2:
            self.assertIn(g._build_answer(update),expected)
            i = i + 1



if __name__ == '__main__':
    unittest.main()