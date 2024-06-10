"""2. Manual Max Function: Define a function named manual_max that iterates through list, 
updating a variable with the maximum value, 
then returns the maximum value found. Use for loop for this task."""

def manual_max(list):
    biggest = list[0]
    for i in list:
        if biggest < i:
            biggest = i
    return biggest

print(manual_max([1,2,3,7,9]))
