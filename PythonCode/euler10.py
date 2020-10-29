#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:37:35 2020

@author: batuhankuru
"""
import time

class CodeTimer:
    def __init__(self, name=None):
        self.name = " '"  + name + "'" if name else ''

    def __enter__(self):
        self.start = time.clock()

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (time.clock() - self.start) * 1000.0
        print('Code block' + self.name + ' took: ' + str(self.took) + ' ms')
sum = 2

def isPrime(n):
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True
if __name__ == "__main__":
    n = 1
    with CodeTimer('loop 1'):
     while n < 2000000:
        n += 2
        if isPrime(n):sum += n
print (sum)
