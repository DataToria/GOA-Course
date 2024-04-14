"""დავალება4) მომხმარებელს შეეკითხეთ ორი მთელი რიცხვი, შემდეგ ამ ორი ცვლადიდან for ციკლში 
უმცირესი ჩასვის start-ის, ხოლო უდიდესი end-ის პოზიციაზე, step არ გინდათ. 
ახლა ჩაურთეთ if statement და დაპრინტეთ მარტო ხუთის ჯერადები."""


num = int(input("enter num: "))
num_2= int(input("enter num: "))
for i in range (num, num_2):
    if i % 5 ==0:
        print(i)