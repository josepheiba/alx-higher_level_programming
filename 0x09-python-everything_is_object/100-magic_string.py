#!/usr/bin/python3
"""docs"""


def magic_string():
    """docs"""
    School()
    return ", ".join(["BestSchool"] * School.number_of_instances)


class School:
    """docs"""
    number_of_instances = 0

    def __init__(self):
        School.number_of_instances += 1
