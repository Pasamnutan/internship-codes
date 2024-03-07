# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:48:32 2024

@author: PASAM
"""

def find_tuple_indices(tuple_list, target_tuples):
    return [i for i, t in enumerate(tuple_list) if t in target_tuples]

# Test the function
tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
target_tuples = [(3, 4), (7, 8), (11, 12)]

indices = find_tuple_indices(tuple_list, target_tuples)
print("Indices of target tuples:", indices)
