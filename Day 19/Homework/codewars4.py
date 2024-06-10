"""https://www.codewars.com/kata/53dc54212259ed3d4f00071c"""
"""Write a function that takes an array of numbers and returns the sum of the numbers.
 The numbers can be negative or non-integer. If the array does not contain any numbers 
 then you should return 0."""



def sum_array(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum
print(sum_array([2,4,6]))