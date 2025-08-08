#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 02:47:05 2025

@author: tgr
"""

def longest_subarray_above_threshold(arr, threshold):
    max_len = 0
    curr_sum = 0
    start = 0
    
    for end in range(len(arr)):
        curr_sum += arr[end]
        while ((curr_sum < threshold * (end - start + 1))
               and start <= end):
            # move start forward
            curr_sum -= arr[start]
            start += 1
        max_len = max(max_len,end - start + 1)
        
    return max_len

