"""Using the map-function with a lambda expression"""

args = [x for x in range(5)]

# converting iterator returned from map to a list
powers_of_2 = list(map(lambda x: 2 ** x, args))
print(powers_of_2)

# getting an iterator from map to loop over
for x in map(lambda x: x * x, powers_of_2):
    print(x, end=' ')
print()
