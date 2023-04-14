"""Simple Generator-Object with function and yield"""

def squares(n):
    for i in range(n):
        yield (i+1) * (i+1)

for number in squares(10):
    print(number, end=", ")