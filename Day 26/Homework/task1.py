"""1. Manual Sum Function: Create a function called manual_sum that iterates over
 list and adds their sum in a variable,
 then returns variable. Use for loop for this task."""


def manual_sum(list):
    x = 0
    for i in list:
        x += i
    return x 
print(manual_sum([25, 60, 70]))
