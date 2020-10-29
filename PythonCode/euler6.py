#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:43:21 2020

@author: batuhankuru
"""

numara=2
sayac=0
inci=0
while(1):
    for i in range(numara,0,-1):
        if(numara%i==0):
            sayac+=1
    if(sayac==2):
        print(numara)
        inci+=1
        print(inci)
    sayac=0
    numara+=1