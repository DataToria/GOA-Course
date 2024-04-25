"""Ask user for five names (use input five times). 
Add all of them in one list and print only first three names.
"""

list =[]
name1 = input("enter name: ")
name2 = input("enter name: ")
name3 = input("enter name: ")
name4 = input("enter name: ")
name5 = input("enter name: ")
list.append(name1)
list.append(name2)
list.append(name3)
list.append(name4)
list.append(name5)
print(list[0:3])