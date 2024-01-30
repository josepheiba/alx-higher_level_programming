#!/usr/bin/python3
def magic_string():
    School()
    return ', '.join(['BestSchool'] * School.number_of_instances)
class School:
    number_of_instances = 0
    def __init__(self):
        School.number_of_instances += 1
