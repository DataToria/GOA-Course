"""3. Manual Min Function: Define a function named manual_min that iterates through list, 
updating a variable with the minimum value, 
then returns the minimum value found. Use for loop for this task."""

def manual_min(list):
    smallest = list[0]
    for i in list:
        if smallest > i:
            smallest = i
    return smallest
print(manual_min([2,4,2,7,1,0,1257]))