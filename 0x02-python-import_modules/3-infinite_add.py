#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sm = 0
    argc = len(sys.argv)
    for i in range(1, argc):
        sm = sm + int(sys.argv[i])
    print("{}".format(sm))
