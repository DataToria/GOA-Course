"""Complete the solution so that it returns true if the first argument(string)
 passed in ends with the 2nd argument (also a string)."""

"""https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python"""


def solution(string, ending):
    if len(ending) > len(string):
        return False
    return string[-len(ending):] == ending

print(solution('abc', 'bc'))