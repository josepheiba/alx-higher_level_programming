#!/usr/bin/python3
def no_c(my_string):
    s = list(x for x in my_string if x not in "Cc")
    return ("".join(s))
