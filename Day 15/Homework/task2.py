"""Create a while loop that asks the user to enter a password. Keep asking until they enter the 
correct password "Goa best". Also print the count of incorrect passwords."""


count = 1

password = input("enter password: ")
while password != "Goa best":
    password = input("enter password: ")
    count += 1
    print(count)

    
    

