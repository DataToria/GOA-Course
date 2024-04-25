"""Write a function that takes a list of numbers as
 input and returns the sum of all the numbers in the list."""



def func (list):
    sum = 0
    for i in list:
        sum += i
    return sum




print(func([5, 7, 9, 12, 23]))
print(func([5, 7, 9, 12, 25, 45,  23]))

    
  
