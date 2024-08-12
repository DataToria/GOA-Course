"""https://www.codewars.com/kata/5259b20d6021e9e14c0010d4"""

"""Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained."""

def reverse_words(s):
    words= s.split(' ')
    reverse_words =[word[::-1] for word in words]
    return ' '.join(reverse_words)
result = reverse_words("Hello World")
print(result)    
        