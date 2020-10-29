#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 23:48:43 2020

@author: batuhankuru
"""


list=[]
def kntrl(x):
    
    sayac=0
    tik=0
    y=str(x)
    ktersi=0
    
    for k in range(len(y)-1,-1,-1):
            if(y[k]==y[ktersi]):
                sayac=sayac+1;
              
            ktersi=ktersi+1;
    if(sayac==len(y)):
        b= int(y)
        return b
    else:
        return 0


for l in range(100,1000,1):
    for m in range(999,101,-1):
       list.append (kntrl(l*m))
print(max(list))
