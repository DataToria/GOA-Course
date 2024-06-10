"""Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types."""

"""https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python"""

def find_short(s):
    list = s.split(" ")
    len_list = []
    for i in list:
        len_list.append(len(i))
    return min(len_list)

print((find_short("Luka Data San Jakob Joe")))
   

