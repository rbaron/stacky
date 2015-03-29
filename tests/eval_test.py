import unittest

from stacky.eval import eval
from stacky.eval import InvalidExpression, InvalidVariableName, InvalidToken
from stacky.env import make_env
from stacky.func import Func


class EvalTest(unittest.TestCase):
    def setUp(self):
        self.env = make_env()

    def test_it_works_with_addition(self):
        tokens = ["5", "3", "+"]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, 8.0)

    def test_it_works_with_subtraction(self):
        tokens = ["10", "12", "-"]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, -2.0)

    def test_it_works_with_division(self):
        tokens = ["1", "2", "/"]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, 0.5)

    def test_it_works_with_multiplication(self):
        tokens = ["3", "5", "*"]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, 15.0)

    def test_it_works_with_min(self):
        tokens = ["3", "5", "min"]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, 3.0)

    def test_it_works_with_max(self):
        tokens = ["3", "-5", "max"]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, 3.0)

    def test_it_works_with_variable_assignment(self):
        tokens = ["5", "a", "="]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, None)
        self.assertEqual(self.env["a"], 5)

    def test_it_raises_for_invalid_variable_names(self):
        for var_name in ["defstack", "[", "]", "1", "list", "set"]:
            tokens = ["5", var_name, "="]
            with self.assertRaises(InvalidVariableName):
                ret = eval(tokens, self.env)

    def test_it_raises_for_malformed_expressions(self):
        expressions = ["4 3 + = ", "1 2 3 min", "0 max"]
        for expression in expressions:
            tokens = expression.split()
            with self.assertRaises(InvalidExpression):
                eval(tokens, self.env)

    def test_it_works_with_stacked_operations(self):
        tokens = ["5", "3", "+", "4", "-"]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, 4.0)

    def test_it_assigns_variable_and_evaluates_function_call(self):
        tokens = ["5", "var_name", "=", "4", "var_name", "-"]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, -1)

    def test_it_assigns_results_of_function_call_to_variable(self):
        tokens = ["5", "1", "min", "var_name", "="]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, None)
        self.assertEqual(self.env["var_name"], 1)

    def test_it_adds_a_new_stack_with_the_right_name(self):
        tokens = ["|", "a", "b", "+", "|", "my_fun", "defstack"]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, None)
        self.assertEqual(self.env["my_fun"].call_stack, ["a", "b", "+"])

    def test_it_calls_a_function_by_extending_the_evaluation_stack_in_the_global_env(self):
        tokens = "5 a = 8 b = my_fun".split()
        self.env.update({
            "my_fun": Func(["a", "b", "-"]),
        })
        ret = eval(tokens, self.env)
        self.assertEqual(ret, -3)

    def test_it_works_with_subsequent_user_defined_functions(self):
        tokens = ["user_defined_subtraction", "b", "=", "user_defined_division"]
        self.env.update({
            "user_defined_subtraction": Func(["a", "b", "-"]),
            "user_defined_division": Func(["a", "b", "/"]),
            "a": 5,
            "b": 8,
        })
        ret = eval(tokens, self.env)
        self.assertEqual(ret, -5/3)

    def test_it_adds_new_stack_and_go_on_with_program(self):
        tokens = ["|", "a", "b", "+", "|", "my_fun", "defstack", "5", "8", "-"]
        ret = eval(tokens, self.env)
        self.assertEqual(ret, -3.0)
        self.assertEqual(self.env["my_fun"].call_stack, ["a", "b", "+"])
