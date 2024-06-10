"https://www.codewars.com/kata/558fc85d8fd1938afb000014"
"""Create a function that returns the sum of the two lowest positive numbers given an 
array of minimum 4 positive integers. 
No floats or non-positive integers will be passed."""

def sum_two_smallest_numbers(numbers):
    first_smallest = None
    second_smallest = None 
    for num in numbers: 
        if not first_smallest or num < first_smallest: 
            second_smallest = first_smallest
            first_smallest = num 
        elif not second_smallest or num < second_smallest: 
            second_smallest = num 
    return first_smallest + second_smallest
    
print(sum_two_smallest_numbers([2,4,5,7,9,10,15,]))
