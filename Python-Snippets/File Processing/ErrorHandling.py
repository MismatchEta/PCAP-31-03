"""Example for dealing with errors while processing files (no with)"""

from os import strerror # returns a string describing the meaning of an error number
## import errno # module with constants for error numbers

try:
    s = open(".\\wrong\\path", "rt") # Wrong path, errno = 2 (errno.ENOENT)
    # Some processing
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))
    print(exc.errno)


