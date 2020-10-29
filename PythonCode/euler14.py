#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 21:24:19 2020

@author: batuhankuru
"""

def zinciruzunlugu(x):
    zincir=0
    while(x>1):
        if(x%2==0):
            x=x/2
            zincir+=1
        else:
            x=3*x+1
            zincir+=1
    return zincir
maxzincir=0
maxzincirdegeri=""
depo=0
for i in range(1000000,0,-1):
    depo=zinciruzunlugu(i)
    if(maxzincir<depo):
        maxzincir=depo
        maxzincirdegeri=i
print(maxzincir,maxzincirdegeri)