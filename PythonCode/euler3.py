#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:28:12 2020

@author: batuhankuru
"""

a=600851475143;
x=2;
liste=[];
while(1):
    if(a%x==0):
        liste.append(x);
        a=a/x;
        print(liste);
    else:
        x=x+1;
    if(a==1):
        break
print(liste);
