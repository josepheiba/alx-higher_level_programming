#!/usr/bin/python3
"""docs"""


def pascal_triangle(n):
    """docs"""
    if n <= 0:
        return []

    tris = [[1]]
    while len(tris) != n:
        tri = tris[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        tris.append(tmp)
    return tris
