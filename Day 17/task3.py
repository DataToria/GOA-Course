"""Write a function that takes a list of numbers as input and returns a
 new list containing only the even numbers from the original list."""



def func(list):
    list2 = []
    for i in list:
        if i % 2 ==0:
            list2.append(i)
    return list2

print(func([2, 3, 7, 9, 10, 12, 14, 18, 21, 23, 28, 25, 45, 50]))
