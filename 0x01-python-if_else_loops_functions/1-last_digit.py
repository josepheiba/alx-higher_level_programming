#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if(number < 0):
    lastDigit = int(str(number)[-1]) * -1
else:
    lastDigit = int(str(number)[-1])
str1 = "Last digit of"
str2 = "and is greater than 5"
str3 = "and is 0"
str4 = "and is less than 6 and not 0"
if(lastDigit > 5):
    print(f"{str1} {number:d} is {lastDigit} {str2}")
elif(lastDigit == 0):
    print(f"{str1} {number:d} is {lastDigit} {str3}")
else:
    print(f"{str1} {number:d} is {lastDigit} {str4}")
