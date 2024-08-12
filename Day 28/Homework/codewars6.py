"""https://www.codewars.com/kata/5208f99aee097e6552000148"""

"""Complete the solution so that the function will break up camel casing, 
using a space between words."""

def solution(s):
    result = ""
    for char in s:
        if char != char.upper():
            result+=char
        else:
            result+= " " + char
    return result

