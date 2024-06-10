"""Implement a function that accepts 3 integer values a, b, c. The function should return 
true if a triangle can be built with the sides of given length and 
false in any other case."""

"""https://www.codewars.com/kata/56606694ec01347ce800001b"""


def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
print(triangle(4, 5, 7))

