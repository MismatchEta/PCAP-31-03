from os import strerror

try:
    bf = open('.\\newbytefile.bin', 'rb') # 'rb' = 'r'ead 'b'ytes
    data = bytearray(bf.read())
    bf.close()

    # Print the contents of the bytearray as hex
    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

