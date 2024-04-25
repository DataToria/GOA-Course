"""Write a function that takes a list of strings as input and returns a new list 
containing only the strings that start with the letter 'A'."""


def func(list):
    list2 = []
    for i in list:
        if i[0]=="A":
            list2.append(i)
    return list2
print(func(["Georgia", "Spain", "Argentina", "Algire", "USA","Italy","Armenia", "Germany"]))

    