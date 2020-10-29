#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 23:03:07 2020

@author: batuhankuru
"""

def faktoriyel(n):
    # base case
    if n == 0:
        return 1
    # recursive case
    else:
        # burada n değerimiz n(n-1)! formülünde gördüğümüz üzere sabit olacağından recursive edilecek kısmı n ile çarpıyoruz.
        # recursive olan kısım ise (n-1)! kısmı olacağından dolayı yinelenen kısmı fonksiyonumuzu tekrar çağırarak faktoriyel(n-1) şeklinde yazıyoruz.
        return n * faktoriyel(n-1)
def hesap():
    a=faktoriyel(100)
    toplam=0
    b=str(a)
    for i in range(len(str(a))):
        toplam+=int(b[i])
    print(toplam)