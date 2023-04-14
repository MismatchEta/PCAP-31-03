"""Examples of a closure"""

# Example 1: Storing a local variable for global use
print("Example 1:")
def outer(val):
    loc = val
    def inner():
        return loc
    return inner

var = outer(3)
print(var) # <class 'function'>
print(var()) # function call of inner-function with loc=3...returns 3
print()

# Example 2: Modify power function with a value from surrounding function
print("Example 2:")
def closure(par):
    loc = par
    def power(p):
        return p ** loc
    return power


squared = closure(2)
cubed = closure(3)

for i in range(5):
    print(i, squared(i), cubed(i), sep=" | ")
