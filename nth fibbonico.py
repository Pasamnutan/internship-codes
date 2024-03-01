# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:55:25 2024

@author: PASAM
"""

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = int(input("Enter the value of n: "))
print(f"The {n}-th Fibonacci number is: {fibonacci_iterative(n)}")