# from commands import command
import unittest
from commands import command

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

    # def test_roll(self):
        # TODO
        # c = Roller(
        #     '',
        #     '',
        #     '',
        #     None
        # )
        # context = Mock()
        # test_vals = [
        #     ('1d4', )
        # ]
        # context.args
        # self.assertTrue()

if __name__ == '__main__':
    unittest.main()