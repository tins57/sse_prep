#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 02:42:26 2025

@author: tgr
"""

class LogAggregator:
    # with rate limiting
    def __init__(self):
        self.last_seen = {}
        
    def should_print_message(self, timestamp, message):
        if (message not in self.last_seen 
            or timestamp - self.last_seen[message] >= 10):
            self.last_seen[message] = timestamp
            return True
        
        return False