#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if (a < b):
            print("{}".format(str(a) + str(b)) + ", ", end="")
        if (a is 8 and b is 9):
            print("{}".format(str(a) + str(b)))
