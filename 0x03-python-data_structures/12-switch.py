#!/usr/bin/python3
a = 89
b = 10
a, b = b, a # switch value by unpacking
print("a={:d} - b={:d}".format(a, b))
