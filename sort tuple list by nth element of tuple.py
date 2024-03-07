# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:45:06 2024

@author: PASAM
"""

def sort_tuple_list_by_nth_element(tuple_list, n):
    return sorted(tuple_list, key=lambda x: x[n])

# Test the function
tuple_list = [(1, 5, 3), (7, 2, 4), (9, 1, 6), (3, 8, 2)]
sorted_list = sort_tuple_list_by_nth_element(tuple_list, 1)
print(sorted_list)
