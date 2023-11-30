#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal's triangle of n
"""

def pascal_triangle(n):
    """
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    lst = []
    if n <= 0:
        return lst
    else:
        for i in range(n):
            if len(lst) == 0:
                lst.append([1])
            else:
                new_lst = [1]
                for ii in range(1, len(lst[-1])):
                    new_lst.append(lst[-1][ii] + lst[-1][(ii - 1)])
                new_lst.append(1)
                lst.append(new_lst)
                
        return lst

