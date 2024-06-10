"""5. Copy function of reduce: define a function named manual_reduce that takes a list as input, 
then create an empty list named copied_list to store the copied items inside it. 
Then use for loop to loop over each item in the original list, 
append them to the copied_iterable list. In the end, 
return the copied_iterable after iterating through all items.
finally demonstrate the usage of the manual_reduce function by creating an original list,
 making a copy of it, and printing both the original and copied lists.
"""

def manual_reduce(list):
    result = "["
    copied_list = list
    for i in list:
        result+= str(i)
    result += "] ["
    for i in copied_list:
        result += str(i)
    result += "]"
    return result

print(manual_reduce([5, 4]))