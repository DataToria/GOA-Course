"""https://www.codewars.com/kata/57eae20f5500ad98e50002c5"""
"""Write a function that removes the spaces from the string, then return the resultant string."""


def spaceless(string):
    result = ""
    for char in string:
        if char != " ":
            result += char
    return result
print(spaceless("8 j 8   mBliB8g  imjB8B8  jl  B" ))

            
