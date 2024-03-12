# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:52:18 2024

@author: PASAM
"""

import numpy as np

def calculate_average(tuple_of_tuples):
    return np.mean(tuple_of_tuples, axis=0)

# Original Tuple 1
tuple1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
average1 = calculate_average(tuple1)
print("Original Tuple:")
print(tuple1)
print("Average value of the numbers of the said tuple of tuples:")
print(average1)

# Original Tuple 2
tuple2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
average2 = calculate_average(tuple2)
print("\nOriginal Tuple:")
print(tuple2)
print("Average value of the numbers of the said tuple of tuples:")
print(average2)