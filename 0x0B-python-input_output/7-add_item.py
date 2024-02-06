#!/usr/bin/python3
"""docs"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fileName = 'add_item.json'
try:
    myList = load_from_json_file(fileName)
except FileNotFoundError:
    myList = []

save_to_json_file(myList.extend(sys.argv[1:]), fileName)
