"""Implement a simple calculator that takes two numbers and an operator (+, -, *, /)
 as input from the user and performs the corresponding operation. Bonus task if you want, 
 it's not necessary - add degree (ხარისხი), use ** operator for it.
"""

num1 = int(input("enter num: "))
num2 = int(input("enter num: "))
operator = input("enter operator: ")
if operator == "+":
    print (num1 + num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "**":
    print(num1 ** num2)
else:
    pass
