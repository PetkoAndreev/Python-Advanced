from functools import reduce


def operate(operator, *args):
    return reduce(mapper[operator], args)


mapper = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}
print(operate("+", 1, 2, 3))