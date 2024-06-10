"""Make a program that filters a list of strings and returns a list with only your 
friends name in it. If a name has exactly 4 letters in it, 
you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not..."""

"""https://www.codewars.com/kata/55b42574ff091733d900002f"""

def friend(x):
    True_friend = []
    Foe=[]
    for i in x:
        if len(i) == 4:
            True_friend.append(i)
        
    return True_friend
   

print(friend(["Ryan", "Kieran", "Mark"]))
        
