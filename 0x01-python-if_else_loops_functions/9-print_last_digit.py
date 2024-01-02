#!/usr/bin/python3
def print_last_digit(number):
    digit = str(number)[-1]
    if (ord(digit) < 58 and ord(digit) > 47):
        print(digit, end="")
        return (digit)
    return (0)
