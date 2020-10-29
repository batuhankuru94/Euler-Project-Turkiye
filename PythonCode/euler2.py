#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:32:02 2020

@author: batuhankuru
"""

x=1
y=1
toplam=x+y
kontrol=x+y
kontrol=0
while 1:
        z=x+y
        x=y
        y=z
        kontrol+=z
        if kontrol<=4000000:
            toplam+=z
        else:
            break
            
print(toplam)
