import unittest
import stacky

from stacky import func

from stacky.func import Func, BuiltinFunc, UserDefinedFunc


class FuncTest(unittest.TestCase):
    def test_creating_Func_instance_raise_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            my_func = Func()


class BuiltInFuncTest(unittest.TestCase):
    def test_it_returns_the_right_number_of_arguments_1(self):
        sum_ = BuiltinFunc(lambda x, y: x+y)
        self.assertEqual(sum_.n_args, 2)

    def test_it_returns_the_right_number_of_arguments_2(self):
        sum_div = BuiltinFunc(lambda x, y, z: (x+y)/z)
        self.assertEqual(sum_div.n_args, 3)

    def test_it_calls_the_lambda_upon_instance_call(self):
        sum_ = BuiltinFunc(lambda x, y: x+y)
        self.assertEqual(sum_(8, 9), 17)


class UserDefinedFuncTest(unittest.TestCase):
    def test_it_returns_the_correct_number_or_args(self):
        sum_ = UserDefinedFunc(["a", "b", "+", "c", "-"], ["a", "b", "c"])
        self.assertEqual(sum_.n_args, 3)

    def test_it_returns_the_call_stack(self):
        sum_ = UserDefinedFunc(["a", "b", "+", "c", "-"], ["a", "b", "c"])
        self.assertEqual(sum_.call_stack, "a b + c -".split())
