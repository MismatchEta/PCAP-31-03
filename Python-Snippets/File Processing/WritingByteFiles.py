"""Example for writing non-text files"""

from os import strerror

# Filling a bytearray with the values from 10 to 19
data = bytearray(10)
for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('.\\newbytefile.bin', 'wb') # 'wb' = 'w'rite 'b'yte
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
