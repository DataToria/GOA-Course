"""Write a program that ask  users to enter a number and then prints whether the number is 
positive, negative, or zero using an if-else statement."""

num = int(input("enter number: "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")