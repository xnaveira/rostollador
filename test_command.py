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



if __name__ == '__main__':
    unittest.main()