"""Counts letters in a file and fives back their frequency in descending order"""
from os import strerror

# Initialize 26 counters for each Latin letter.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")

try:
    # Counting characters
    f = open(file_name, "rt")
    for line in f:
        for char in line:
            # If it is a letter...
            if char.isalpha():
                # ...treat it as lower-case and update the appropriate counter.
                counters[char.lower()] += 1
    f.close()

    # Output
    for char in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        cnt = counters[char]
        if cnt > 0:
            print(char, '->',cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
