import inspect


class Func():
    def __init__(self):
        raise NotImplementedError("Func class needs to be subclassed")

# TODO: how to prettify these inheritances?

class BuiltinFunc(Func):
    def __init__(self, lambda_):
        self.lambda_ = lambda_

    @property
    def n_args(self):
        return len(inspect.getargspec(self.lambda_).args)

    def __str__(self):
        return "Built-in function"

    def __call__(self, *args):
        return self.lambda_.__call__(*args)


class UserDefinedFunc(Func):
    def __init__(self, stack, args):
        self.stack = stack
        self.args = args

    @property
    def n_args(self):
        return len(self.args)

    def __str__(self):
        return "User-defined function"

    @property
    def call_stack(self):
        return self.stack


