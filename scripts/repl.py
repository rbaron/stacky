from stacky.eval import eval, is_num, is_valid_variable
from stacky.eval import UndefinedVariable
from stacky.env import make_env
from stacky.parser import tokenize


if __name__ == "__main__":
    env = make_env()
    expr = input()

    while expr != "exit":
        if is_num(expr):
            print(float(expr))

        elif is_valid_variable(expr):
            try:
                print(env[expr])
            except KeyError:
                print("Undefined variable")

        else:
            ret = eval(tokenize(expr), env)
            if ret:
                print(ret)

        expr = input()

