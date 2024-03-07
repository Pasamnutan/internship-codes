# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:36:39 2024

@author: PASAM
"""

def flatten_tuple_of_lists(tup):
    return [item for sublist in tup for item in (sublist if isinstance(sublist, (list, tuple)) else (sublist,))]

# Test the function
tuple_of_lists = ([1, 2, 3], [4, 5], [6, [7, 8]])
flattened_list = flatten_tuple_of_lists(tuple_of_lists)
print(flattened_list)
