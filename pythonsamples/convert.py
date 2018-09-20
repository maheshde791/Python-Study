#!/usr/bin/python
import binascii

n = '000000000000015af96201103139322e3136382e31302e31313000000000000000000000'
header, data = n[:4], n[20:]
print data
binary_string = binascii.unhexlify(data)
print ''.join(binary_string)
print binascii.a2b_hex(data)