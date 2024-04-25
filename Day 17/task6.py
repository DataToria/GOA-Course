""""Write a function that takes a list of numbers as input and 
returns a new list containing the square of each number."""



def func(list):
    list2 = []
    for i in list:
        print(i**2)
        list2.append(i)

print(func([2, 5, 10, 225, 67, 1]))






