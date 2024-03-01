# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:00:08 2024

@author: PASAM
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_in_interval(start, end):
    print("Prime numbers between", start, "and", end, "are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print_prime_in_interval(start, end)