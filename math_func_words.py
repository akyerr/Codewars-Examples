'''This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Divison should be integer division. For example, this should return 2, not 2.666666...:'''


def zero(*args):
    if len(args) == 0:
        return 0
    else:
        return args[0](0)


def one(*args):
    if len(args) == 0:
        return 1
    else:
        return args[0](1)


def two(*args):
    if len(args) == 0:
        return 2
    else:
        return args[0](2)


def three(*args):
    if len(args) == 0:
        return 3
    else:
        return args[0](3)


def four(*args):
    if len(args) == 0:
        return 4
    else:
        return args[0](4)


def five(*args):
    if len(args) == 0:
        return 5
    else:
        return args[0](5)


def six(*args):
    if len(args) == 0:
        return 6
    else:
        return args[0](6)


def seven(*args):
    if len(args) == 0:
        return 7
    else:
        return args[0](7)


def eight(*args):
    if len(args) == 0:
        return 8
    else:
        return args[0](8)


def nine(*args):
    if len(args) == 0:
        return 9
    else:
        return args[0](9)


def plus(n):
    return lambda x: x + n


def minus(n):
    return lambda x: x - n


def times(n):
    return lambda x: x * n


def divided_by(n):
    return lambda x: x // n


'''def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))'''

'''def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y'''
