#ASSEMBLER
#LABORATORIO 5
#FERNANDO HENGSTENBERG
#CARLOS CHEW

import struct

def bin_to_float(b):
    """ Convert binary string to a float. """
    bf = int_to_bytes(int(b, 2), 8)  
    return struct.unpack('>d', bf)[0]

def int_to_bytes(n, minlen=0): 
    """ Int/long to byte string. """
    nbits = n.bit_length() + (1 if n < 0 else 0) 
    nbytes = (nbits+7) // 8  
    b = bytearray()
    for _ in range(nbytes):
        b.append(n & 0xff)
        n >>= 8
    if minlen and len(b) < minlen:  # zero pad?
        b.extend([0] * (minlen-len(b)))
    return bytearray(reversed(b))  # high bytes first

# tests

def float_to_bin(f):
    """ Convert a float into a binary string. """
    ba = struct.pack('>d', f)
    ba = bytearray(ba)  # convert string to bytearray - not needed in py3
    s = ''.join('{:08b}'.format(b) for b in ba)
    return s[:-1].lstrip('0') + s[0] # strip all leading zeros except for last

for f in 0.0, 1.0, -14.0, 12.546, 3.141593:
    binary = float_to_bin(f)
    print('float_to_bin(%f): %r' % (f, binary))
    float = bin_to_float(binary)
    print('bin_to_float(%r): %f' % (binary, float))
    print('')
