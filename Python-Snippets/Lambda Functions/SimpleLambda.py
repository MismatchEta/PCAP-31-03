"""Example use of a lambda"""

# Takes a list of arguments and function to print a list of (arg -> fun(arg)) pairs
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

# passing lambda as parameter instead of defining a second function
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

