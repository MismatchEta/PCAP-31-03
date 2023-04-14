"""List and Generator with List comprehension"""

import sys

items = 10

# Iterating over a list object
# The whole lists is stored in memory.
lst = [1 if x % 2 == 0 else 0 for x in range(items)]
print(f"List size: {lst.__sizeof__()}")
for v in lst:
    print(v, end=" ")
print()

# Iterating over a generator object
# Only subsequent values are stored
gen = (1 if x % 2 == 0 else 0 for x in range(items))
for v in gen:
    print(v, end=" ")
print()

print ("Size comparison")
for items in [1, 10, 100, 1000, 10000]:
    lst = [1 if x % 2 == 0 else 0 for x in range(items)]
    gen = (1 if x % 2 == 0 else 0 for x in range(items))
    print(f"{items} Items", end =" | ")
    print(f"List: {lst.__sizeof__()}", end=" | ")
    print(f"Generator: {gen.__sizeof__()}")