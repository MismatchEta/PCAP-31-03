"""Example writing text files"""

from os import strerror

try:
    # Opening the stream, creates new file or deletes existing one
    stream = open(".\\newfile.txt", "wt") # 'w'riting file in 't'ext mode
    
    # Writes Hello World as the 1st line and "line # ..." for the lines 2 to 11.
    stream.write("Hello World!\n")
    for i in range(10):
        s = "line #" + str(i+2) + "\n"
        for ch in s:
            stream.write(ch)

    # Closing the stream
    stream.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))
    print(exc.errno)


