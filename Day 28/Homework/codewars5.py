"""https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python"""

"""Given two numbers and an operator operator (the name of it, as a string), 
return the result of the two numbers having that operator used on them.
a and b will both be positive integers, and a will always be the first number in the operation, 
and b always the second.The four operators are "add", "subtract", "divide", "multiply"."""


def arithmetic(a, b, operator):
        if operator == "add":
            return a+b
        elif operator == "minus":
            return a-b
        elif operator =="devide":
            return a/b
        elif operator == "multiply":
            return a*b
print(arithmetic(9,3, "devide"))
print(arithmetic(10,5,"minus" ))
print(arithmetic(10,5,"devide"))
print(arithmetic(10,5,"multiply"))