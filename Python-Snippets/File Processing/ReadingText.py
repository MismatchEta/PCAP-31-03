"""Example reading text files"""

from os import strerror # returns a string describing the meaning of an error number
## import errno # module with constants for error numbers

try:
    # Opening the stream
    stream = open(".\\file.txt", "rt") # 'r'eading file in 't'ext mode
    
    print(stream.read(1)) # Reads one character (whole file if no parameter)
    stream.seek(0) # Sets pointer of stream back to the beginning of the file
    readout = stream.read() # Reads the whole file into a string
    stream.seek(0)
    # Loop to print the text line by line
    for line in stream.readlines():
        print(line, end="")
        input()

    # Closing the stream
    stream.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))
    print(exc.errno)


