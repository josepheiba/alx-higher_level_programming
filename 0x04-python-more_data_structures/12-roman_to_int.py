#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in dic.keys():
            return 0
        elif dic[i] >= dic[j]:
            number += dic[i]
        else:
            number -= dic[i]
    number += dic[roman_string[-1]]
    return number
