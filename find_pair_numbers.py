#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 2025

@author: tagir
"""

import os
import sys
import numpy as np


def int_array(arr):
    read_arr = np.array([], dtype=int)
    try:
        read_arr = np.array(arr, dtype=int)
    except (TypeError, ValueError):
        print(f"Expected an integer array")
    except Exception as e:
        print(f"Unexpected error {e}")
    return read_arr
    

# Given an array of integers, find any two numbers that sum up to a target.
def find_numbers(arr, target):
    # Simple O(n^2) algorithm double loop search

    arr = int_array(arr)
    if arr is None:
        return None 

    # Naive O(n**2) on average search
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
            
    # in case no pair of numbers found
    return None

# More optimized algorithm could exist based on the fact that target and the numers are ints
def find_numbers_version2(arr, target):
    # Optimized algorithm: O(n log n) complexity, space complexity O(n), using pre-sorting
    # Given an array of integers, find any two numbers that sum up to a target.

    arr = int_array(arr)

    arr = sorted(arr) # pre-sort the array O(n log n) complexity

    # To find the required pair, iterate over the first term and
    # try to binary search the matching second number, array O(n log n) complexity
    # binary search or the second term O(n log n)
    for i in range(len(arr)):
        # binary search or the second term O(log n)
        second_term = target - arr[i]
        idx_second = np.searchsorted(arr[i + 1:], second_term)

        if second_term == arr[idx_second]:
            return (arr[i], second_term)

          
    # in case no pair of numbers found
    return None

# Table approach
def find_numbers_version3(arr, target):
    # Hash table O(n) time complexity

    arr = int_array(arr)

    hash_second_required_terms = set()
    for i in range(len(arr)):
        second_term = target - arr[i]
        if arr[i] in hash_second_required_terms:
            return (second_term, arr[i])
        else:
            hash_second_required_terms.add(second_term)

    return None



def main():

    arr = np.arange(5) + 1
    test_sum = 5
    print(f"test array{arr} sum={test_sum}")
     # correct result 1 and 4 or 2 and 3
    print(find_numbers(arr, test_sum)) # correct result 1 and 4
    print(find_numbers_version2(arr, test_sum)) # correct result 4 and 1
    print(find_numbers_version3(arr, test_sum)) # correct result 2 and 3
    print(find_numbers([5], test_sum)) # None
    print(find_numbers([], test_sum)) # None
    # print(find_numbers("abc", test_sum)) # Expected an integer array None



if __name__ == "__main__":
    main()
