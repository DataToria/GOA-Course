"""https://www.codewars.com/kata/515f51d438015969f7000013"""

"""Write a function that when given a number >= 0,
 returns an Array of ascending length subarrays."""


def pyramid(n):
    result = []
    for i in range(1, n+1):
        subarray = [1] * i 
        result.append(subarray)
    return result

print(pyramid(3))