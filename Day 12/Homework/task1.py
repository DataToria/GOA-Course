""""Calculate the sum of all even numbers from 1 to 10 using a while loop:"""

i = 1
even_sum = 0
while i < 11:
    i+=1
    if i % 2 == 0:
        even_sum += i
print(even_sum)


