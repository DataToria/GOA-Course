"""Write a function that takes a list of strings as input and returns 
a new list containing only the strings that have a length greater than 5."""



def func(list):
    list2 = []
    for i in list:
        if len(i) > 5:
            list2.append(i)
    return list2


print(func(["miveaklhleni",  "shematkhves", "mat", "abjar-cmuloba", "katsi", "movida", "momartva", "mefisa",
"motsikuloba"]))

