"""Using the filter-function with a lambda expression"""

from random import seed, randint

seed()
data = [randint(-10,10) for x in range(10)]

# filter the random ints according to lambda (bigger than zero and even) and convert to list
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
