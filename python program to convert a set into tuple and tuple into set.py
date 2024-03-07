# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:38:06 2024

@author: PASAM
"""

# Function to convert set into tuple
def set_to_tuple(input_set):
    return tuple(input_set)

# Function to convert tuple into set
def tuple_to_set(input_tuple):
    return set(input_tuple)

# Test the functions
input_set = {1, 2, 3, 4, 5}
input_tuple = (1, 2, 3, 4, 5)

# Convert set to tuple
converted_tuple = set_to_tuple(input_set)
print("Set converted to tuple:", converted_tuple)

# Convert tuple to set
converted_set = tuple_to_set(input_tuple)
print("Tuple converted to set:", converted_set)
