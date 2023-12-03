#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create a new list with True or False based on whether each element is a multiple of 2
    result_list = [num % 2 == 0 for num in my_list]
    return result_list
