#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 23:02:52 2025

@author: tgr
"""

from collections import deque
import numpy as np


class SensorFilter:
    def __init__(self, k):
        self.k = k
        self.buffer = deque(maxlen=k)
        
    def update(self, reading):
        # handle broken input
        try:
            self.buffer.append(float(reading))
        except (ValueError, TypeError):
            pass
        except Exception as e:
            print(f"An unexpected error: {e}")
        finally:
            return self.get_filtered_average()

    
    def get_filtered_average(self):
        if not self.buffer:
            return None
        arr = np.array(self.buffer)
        mean = np.mean(arr)
        std = np.std(arr)
        print(f'std{std}')
        
        filtered = arr[np.abs(arr - mean) <= 2 * std]
        print(filtered)
        if len(filtered) == 0:
            return mean # fallback to unfiltered
        return np.mean(filtered)
    
    
# import pytest
import unittest
# from sensor_filter import SensorFilter
    
def test_moving_average():
    sf = SensorFilter(k=3)
    assert sf.update(10) == 10.0
    assert sf.update(20) == 15.0
    assert sf.update(30) == 20.0
    assert sf.update(40) == 30.0 # 10 is out of buffer
    
    


# print(sf.update(-2))
# print(sf.update(-2))
# print(sf.update(0))
# print(sf.update(1))
# print(sf.update(3000000))

