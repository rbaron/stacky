"""
    An enviroment is simply a dict that maps keys to values.

        - Keys are strings, which hold the name a variable
        - Values can be:
            * literals (ints only for now)
            * built in functions (+, -, /), implemented as instances of stacky.fun.BuiltinFunc
            * user-defined functions, which are instances of stacky.fun.UserDefinedFunc
"""

from stacky.func import BuiltinFunc

_default_env = {
    "+": BuiltinFunc(lambda x, y: x+y),
    "-": BuiltinFunc(lambda x, y: x-y),
    "/": BuiltinFunc(lambda x, y: x/y),
    "*": BuiltinFunc(lambda x, y: x*y),
    "^": BuiltinFunc(lambda x, y: pow(x,y)),
    "max": BuiltinFunc(lambda x, y: max(x, y)),
    "min": BuiltinFunc(lambda x, y: min(x, y)),
}

def make_env():
    return _default_env.copy()
