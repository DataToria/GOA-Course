"""შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. თქვენ უნდა დააბრუნოთ 
ამ სიის საშუალო არითმეტიკული ( ჯამი / რაოდენობაზე)"""

def func(list):
    sum = 0
    count = 0
    for i in list:
        sum += i
        count +=1
    return sum / count
print(func([1, 2, 4, 3, 5, 6, 8, 7, 9]))
        
        