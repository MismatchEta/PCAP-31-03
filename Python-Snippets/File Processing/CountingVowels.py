"""Function to count vowels in a text"""

from os import strerror

try:
    # Opening the stream
    stream = open(".\\file.txt", "rt")
    
    # Read file character by character
    counter = 0
    for char in stream.read():
        if char in "aeiou":
            counter += 1
    # Closing the stream
    stream.close()

    print(f"There are {counter} vowels in the text.")
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))
    print(exc.errno)



