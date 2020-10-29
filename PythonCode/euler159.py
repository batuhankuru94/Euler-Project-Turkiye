#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 22:12:47 2020

@author: batuhankuru
"""
from itertools import combinations
a=int(input("bir sayi girin"))
sayac=0
liste=[2,3,5,7,9,11,13,17,23,29]
listedp=liste
depo=[]
b=(combinations(liste, 2))
for each in b:
    depo.append(each)
samsarra=0
carp=1
for i in liste:
    carp*=i
for i in depo:
    for j in range(len(depo[0])-1):
        print(i[j],i[j+1],i[j]*i[j+1])

"""
for i in range(a,1,-1):
    if(a%i==0):
        sayac+=1
if(sayac==3):
    sayac-=1
print(sayac)
"""