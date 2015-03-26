import unittest

from stacky import parser


class ParserTest(unittest.TestCase):
    def test_it_tokenizes_a_correct_program(self):
        program = "a b + 4 *"
        tokens = parser.tokenize(program)
        self.assertEqual(tokens, ["a", "b", "+", "4", "*"])
