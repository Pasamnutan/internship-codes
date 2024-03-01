# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:57:11 2024

@author: PASAM
"""

def add_two_numbers(a, b):
    return a + b

def maximum_of_two_numbers(a, b):
    return max(a, b)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = add_two_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {sum_result}")

max_result = maximum_of_two_numbers(num1, num2)
print(f"The maximum of {num1} and {num2} is: {max_result}")