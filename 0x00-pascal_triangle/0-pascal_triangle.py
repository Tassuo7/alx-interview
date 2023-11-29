#!/usr/bin/python3
"""
Pascal's Triangle of n.
"""


def pascal_triangle(n):
    """
    a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return ([])
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    pastri = [[1], [1, 1]]
    for i in range(2, n):
        r = [1]
        for j in range(1, i):
            r.append(pastri[i-1][j-1] + pastri[i-1][j])
        r.append(1)
        pastri.append(r)
    return pastri
