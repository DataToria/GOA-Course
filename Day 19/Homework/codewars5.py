"""https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3"""
"""Write a function to convert a name into initials. This kata strictly takes
 two words with one space in between them.
The output should be two capital letters with a dot separating them."""

def abbrev_name(name):
    abrv = ""
    abrv += name[0].capitalize() + "."
    for i in range(len(name)):
        if name[i] == " ":
            abrv += name[i + 1].capitalize()
    return abrv