# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:40:26 2024

@author: PASAM
"""

def dict_list_to_tuple_list(dict_list):
    return [tuple(dictionary.items()) for dictionary in dict_list]

# Test the function
list_of_dicts = [
    {'a': 1, 'b': 2},
    {'x': 10, 'y': 20},
    {'foo': 'bar', 'baz': 'qux'}
]

tuple_list = dict_list_to_tuple_list(list_of_dicts)
print(tuple_list)
