# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:56:10 2024

@author: PASAM
"""

def convert_dict_value_list_to_dict_list(input_dict):
    def construct_dict(index):
        return {key: input_dict[key][index] for key in input_dict.keys()}

    dict_list = [construct_dict(i) for i in range(len(next(iter(input_dict.values()))))]
    return dict_list

# Test the function
input_dict = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}

dict_list = convert_dict_value_list_to_dict_list(input_dict)
print(dict_list)
