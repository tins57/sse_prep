#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 02:21:17 2025

@author: tgr
"""

import threading
import time

class Worker(threading.Thread):
    def __init__(self, worker_id, heartbeat_dict, heartbeat_frequency=0.00001):
        super().__init__()
        self.worker_id = worker_id
        self.heartbeat_dict = heartbeat_dict
        self.heartbeat_frequency = heartbeat_frequency
        self.running= True
        
    def run(self):
        while self.running:
            self.heartbeat_dict[self.worker_id] = time.time()
            time.sleep(self.heartbeat_frequency)
            
    def stop(self):
        self.running = False

class Watchdog:
    def __init__(self, num_workers=3, timeout=1.0, frequency=1.0):
        self.timeout = timeout
        self.heartbeat_dict = {}
        self.frequency = frequency
        self.workers = [self.spawn_worker(i) for i in range(num_workers)]
        
    def spawn_worker(self, worker_id):
        worker = Worker(worker_id, self.heartbeat_dict)
        worker.daemon = True
        worker.start()
        return worker
        
    def monitor(self):
        while True:
            now = time.time()
            for i, w in enumerate(self.workers):
                last_beat = self.heartbeat_dict.get(i, 0)
                if now - last_beat > self.timeout:
                    print(f"[Watchdog] Restarting worker {i}")
                    w.stop()
                    self.workers[i] = self.spawn_worker(i)
            time.sleep(self.frequency)

wdog = Watchdog(timeout=0.00001)
wdog.monitor()