"""Write a function that takes a list of strings as input and returns a
 new list containing the lengths of each string."""

def func(list):
    list2 = []
    for i in list:
        list2.append(len(i))
    return list2
print(func(["Georgia", "Spain", "Argentina", "Algire", "USA","Italy","Armenia"]))
    



