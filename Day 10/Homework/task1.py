# (მოხმარებელს შემოატანინეთ პაროლი იქამდე სანამ არ დაემთხვევა რეგისტრირებულ პაროლს, while ციკლის და  if else _ის გამოყენებით) 

password = input('password: ')
if password =="argetyvi":
        print("access gained")
while password != "argetyvi":
        print("incorrect password, renter you're password: ")
        password = input('password: ')
print("Access granted")