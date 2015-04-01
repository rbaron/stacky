# stacky

stacky is a programming language with a [RPN](http://en.wikipedia.org/wiki/Reverse_Polish_notation)-like syntax. It is currently under development. Right now, the only supported type is numeric (python equivalent to `float`).

### Applying a function
```
> 5 8 -
-3.0
```
Python equivalent:
```
5 - 8
```

### Defining a variable
```
> 5 a =
> a
5.0
```
Python equivalent:
```
a = 5
```

### Assigning the result of an expression to a variable
```
> 5 8 / c =
> c
0.652
```
Python equivalent:
```
c = 5 / 8
```

### Defining a function
This is a particularly cool thing in the language. In order to define a function, you should explicitly define what its stack looks like. The syntax is:

    | function_stack | args function_name defstack

Example:
```
> | a b / | a b my_division defstack
> 5 8 my_division
0.625
```
Python equivalent:
```
def my_division(a, b):
    return a/b
my_division(5, 8)
```

## Installation

### Via pypi (python3)
```
$ pip install stacky
```

## Opening the interactive interpreter (REPL)
```
$ istacky
istacky: stacky interective interpreter! Type :h for help

> 5 8 /
0.625
```

