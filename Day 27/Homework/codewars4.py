"""You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. 
If the word's length is even, return the middle 2 characters."""

"""https://www.codewars.com/kata/56747fd5cb988479af000028/train/python"""

def get_middle_character(word):
    length = len(word)
    middle = length // 2
    if length % 2 == 0:
        return word[middle - 1: middle + 1]
    else:       
        return word[middle]
print(get_middle_character("datat"))