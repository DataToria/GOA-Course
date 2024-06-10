"""https://www.codewars.com/kata/57f781872e3d8ca2a000007e"""

"""Given an array of integers, return a new array with each value doubled."""

def maps(a):
    list = []
    for i in a:
        list.append(i * 2)
    return list
print(maps([4,5,6]))