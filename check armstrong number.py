# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:59:23 2024

@author: PASAM
"""

def is_armstrong_number(num):
    num_digits = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits
        temp //= 10
    return num == sum
num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")