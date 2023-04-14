"""Script to copy a file"""

from os import strerror

# open source file
srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

# open/create destination file (no checking if file exists already)
dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536) # 64kB buffer to read from src
total  = 0

# read from src and write to dst
try:
    readin = src.readinto(buffer) # readinto returns number of bytes read
    while readin > 0:
        written = dst.write(buffer[:readin]) # don't write last bytes if buffer isn't full
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	

# clean up
print(total,'byte(s) succesfully written')
src.close()
dst.close()
