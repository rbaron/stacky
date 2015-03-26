import inspect


class InvalidExpression(Exception):
    pass


def eval(tokens, env):
    """
        Evaluates an expression in a given enviroment. For every token in expression:

            - Token is a variable attribution (=)
                * Pop two items from the evaluation stack: variable name (str), value (int)
                * Sets enviroment[variable_name]: value

            - Token is a literal (for now, only int)
                * Append literal to evaluation stack

            - Lookup token in enviroment

                - Token is there

                    - It's a function
                        * Pop the function's number of args off the stack
                        * Append the result of calling the function with the
                            popped args back to the stack

                    - It's a 'regular' variable
                        * Append the value of that variable to the stack

                - Token is not there
                    * Append the token (str) to the stack, because maybe a "="
                        will come afterwards and define that symbol on the enviroment


    """
    stack = []

    for token in tokens:

        if token == "=":
            var_name = stack.pop()
            var_value = stack.pop()
            env[var_name] = var_value

        else:
            try:
                stack.append(int(token))
            except ValueError:
                try:
                    var = env[token]

                    # It's a function: pop args and append call result
                    if hasattr(var, "__call__"):
                        n_args = len(inspect.getargspec(var).args)

                        args = [stack.pop() for  i in range(n_args)]

                        # 3 8 - actually means 3 - 8, which means diff(3, 8)
                        args.reverse()

                        stack.append(var(*args))

                    # It's a 'regular' variable
                    else:
                        stack.append(var)

                except KeyError:

                    # Variable is not defined. Append the symbol itself
                    stack.append(token)

    #if len(stack) > 0:
    #    raise InvalidExpression

    return stack

