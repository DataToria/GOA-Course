"""Write a function that takes a list of numbers as input and returns the sum of 
all the numbers that are greater than 10"""

def func(list):
    sum = 0
    for i in list:
        if i > 10:
            sum += i
    return sum

print(func([2, 5, 10, 225, 67, 1]))