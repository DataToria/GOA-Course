
"""Write a program that asks the user to enter a password. 
If the password is "abc123", print "Access granted"; otherwise, print "Access denied"."""

pas="abc123"
password=input("enter password: ")
if password==pas:
    print("access granted")
else:
    print("access denied")
