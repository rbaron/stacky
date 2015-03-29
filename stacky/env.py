"""
    An enviroment is simply a dict that maps keys to values.

        - Keys are strings, which hold the name a variable
        - Values can be:
            * literals (ints only for now)
            * built in functions (+, -, /), implemented as lambdas
            * user-defined functions, which are instances of stacky.fun.Func
"""

_default_env = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "/": lambda x, y: x/y,
    "*": lambda x, y: x*y,
    "&": lambda x, y: x&y,
    "|": lambda x, y: x|y,
    "^": lambda x, y: x^y,
    "max": lambda x, y: max(x, y),
    "min": lambda x, y: min(x, y),
}

def make_env():
    return _default_env.copy()
