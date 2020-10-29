#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 03:32:41 2020

@author: batuhankuru
"""

import math
x=(str(int(math.pow(2,1000))))
y=0
for i in range(0,len(x)):
    y+=int(x[i])
print(y)