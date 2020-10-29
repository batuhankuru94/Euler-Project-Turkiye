#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 23:19:41 2020

@author: batuhankuru
"""
def pbstop (x):
    toplam=0
    for i in range(1,x,1):
        if(x%i==0):
            toplam+=i
    return toplam
def terspbstop (x):
    toplam=0
    for i in range(1,x,1):
        if(x%i==0):
            toplam+=i
    return toplam
liste=[]
for i in range(1,10000,1):
    a=pbstop(i)
    b=pbstop(a)
    if(b==i and i!=a):
        liste.append(i)
        print(i)
print(sum(liste))
    