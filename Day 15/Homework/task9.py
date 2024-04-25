"""Using for loop, ask user for number. Then create a new_list which will
 have even numbers in next range: from 0 to user's number. 
 At last, print out whole new_list. """


new_list =[]
users_num = int(input("enter num: "))
for i in range (0, users_num):
    if i % 2 == 0:
        new_list.append(i)
print(new_list)

