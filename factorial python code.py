# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:52:13 2024

@author: PASAM
"""

def factorial(n):
    """
    Calculate the factorial of a number using recursion
    :param n: integer number
    :return: factorial of the number
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
number = int(input("Enter a number: "))

result = factorial(number)
print("Factorial of", number, "is", result)