"""Ask user to enter name and print the last character of that string."""

list = []
name = input("enter name: ")
list.append(name)
for i in list:
    print(i[-1])