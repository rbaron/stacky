import unittest

from stacky.eval import eval
from stacky.env import env


class EvalTest(unittest.TestCase):
    def setUp(self):
        self.env = env.copy()

    def test_it_works_with_addition(self):
        tokens = ["5", "3", "+"]
        stack = eval(tokens, self.env)
        self.assertEqual(stack, [8])

    def test_it_works_with_subtraction(self):
        tokens = ["10", "12", "-"]
        stack = eval(tokens, self.env)
        self.assertEqual(stack, [-2])

    def test_it_works_with_division(self):
        tokens = ["1", "2", "/"]
        stack = eval(tokens, self.env)
        self.assertEqual(stack, [0.5])

    def test_it_works_with_multiplication(self):
        tokens = ["3", "5", "*"]
        stack = eval(tokens, self.env)
        self.assertEqual(stack, [15])

    def test_it_works_with_min(self):
        tokens = ["3", "5", "min"]
        stack = eval(tokens, self.env)
        self.assertEqual(stack, [3])

    def test_it_works_with_max(self):
        tokens = ["3", "-5", "max"]
        stack = eval(tokens, self.env)
        self.assertEqual(stack, [3])

    def test_it_works_with_variable_assignment(self):
        tokens = ["5", "a", "="]
        stack = eval(tokens, self.env)
        self.assertEqual(stack, [])
        self.assertEqual(self.env["a"], 5)

    def test_it_works_with_stacked_operations(self):
        tokens = ["5", "3", "+", "4", "-"]
        stack = eval(tokens, self.env)
        self.assertEqual(stack, [4])

    def test_it_assigns_variable_and_evaluates_function_call(self):
        tokens = ["5", "var_name", "=", "4", "var_name", "-"]
        stack = eval(tokens, self.env)
        self.assertEqual(stack, [-1])

    def test_it_assigns_results_of_function_call_to_variable(self):
        tokens = ["5", "1", "min", "var_name", "="]
        stack = eval(tokens, self.env)
        self.assertEqual(stack, [])
        self.assertEqual(self.env["var_name"], 1)

