"""Write a function that takes a list of numbers 
as input and returns the largest number in the list."""



def func(list):
    biggest =list[0]
    for i in list:
        if biggest < i:
            biggest = i
    return  biggest
print(func([60, 1, 7, 9, 10, 17, 25, 35, 40, 5, 18, 23, 50, 57]))
    
