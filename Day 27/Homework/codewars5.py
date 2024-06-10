"""In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number."""

"""https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python"""

def high_and_low(numbers):
    numbers_list = list(map(int, numbers.split()))
    high = max(numbers_list)
    low = min(numbers_list)
    return f"{high} {low}"

print(high_and_low("1 2 3 4 5")) 
print(high_and_low("1 9 3 4 -5"))  
print(high_and_low("42 42"))       