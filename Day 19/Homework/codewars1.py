"""https://www.codewars.com/kata/55a2d7ebe362935a210000b2"""

"""Given an array of integers your solution should find the smallest integer.

For example:"""



def func(list):
    smallest = list[0]
    for i in list:
        if smallest > i:
            smallest = i
    return smallest
print(func([2, 4, 6, 6, 1]))
