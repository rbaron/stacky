import inspect
import re

from itertools import takewhile

from stacky.func import BuiltinFunc, UserDefinedFunc


class InvalidExpression(Exception):
    pass


class InvalidVariableName(Exception):
    pass


class InvalidToken(Exception):
    pass


class UndefinedVariable(Exception):
    pass


def is_num(token):
    try:
        return isinstance(float(token), float)
    except ValueError:
        return False


def is_valid_variable(token):
    regex = "^[_a-zA-Z]+[_0-9a-zA-Z]*$"
    reserved_words = "defstack max min list set eval".split()
    return re.match(regex, token) and token not in reserved_words


def _get_value(token, env):
    if is_num(token):
        return float(token)
    elif is_valid_variable(token):
        try:
            return env[token]
        except KeyError:
            raise UndefinedVariable(token)
    else:
        raise InvalidToken(token)


def eval(tokens, env):

    stack = []

    itertokens = iter(tokens)

    for token in itertokens:

        # Variable assignment
        if token == "=":
            try:
                var_name = stack.pop()
                var_value = stack.pop()
            except IndexError:
                raise InvalidExpression("Invalid variable assignment syntax")

            if not is_valid_variable(var_name):
                raise InvalidVariableName(var_name)
            else:
                env[var_name] = _get_value(var_value, env)

        # User-defined function definition
        elif token == "|":
            func_stack = list(takewhile(lambda t: t != "|", itertokens))
            func_args = list(takewhile(lambda t: t != "defstack", itertokens))

            try:
                func_name = func_args.pop()
            except IndexError:
                raise InvalidExpression("Invalid defstack syntax")
            env[func_name] = UserDefinedFunc(func_stack, func_args)

        # Builtin function call
        elif token in env and isinstance(env[token], BuiltinFunc):
            try:
                args = [_get_value(stack.pop(), env) for  i in range(env[token].n_args)]
            except IndexError:
                raise InvalidExpression("Not enough operands on the stack")

            args.reverse()
            stack.append(env[token](*args))

        # User defined function call
        elif token in env and isinstance(env[token], UserDefinedFunc):

            # TODO: implement an enviroment inheritance scheme instead of copying
            subenv = env.copy()
            subenv.update({
                arg: _get_value(stack.pop(), env)
                for arg in env[token].args[::-1]
            })
            stack.append(eval(env[token].call_stack, subenv))

        # It's either a literal or a variable name
        else:
            stack.append(token)

    if len(stack) > 1:
        raise InvalidExpression("Stack leftover: {}".format(stack))

    return _get_value(stack.pop(), env) if stack else None

