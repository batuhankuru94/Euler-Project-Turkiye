#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 23:11:40 2020

@author: batuhankuru
"""
rakamlar=["one","two","three","four","five","six","seven","eight","nine"]
rakamlar=["one","two","three","four","five","six","seven","eight","nine"]
onlar=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
y_onlar=["ten","eleven","twelve","thirteen","fourteen","sixteen","seventeen","eighteen","nineteen"]
listesayici=[]
for i in range(1,1000,1):
    j=i
    a=i
    kstring=str(a)
    if(len(kstring)==3):
        if(kstring[-2]!="1"):
            b=(a-a%100)/100
            listesayici.append(rakamlar[int(b-1)])
            listesayici.append("hundred")
            c=a%10
            c=a-c
            c=(c%100)/10
            d=a%10
            if(c!=0 or d!=0):
                listesayici.append("and")
            if(c!=0):
                listesayici.append(onlar[int(c-1)])
            if(d!=0):
                listesayici.append(rakamlar[int(d-1)])
        else:
            b=(a-a%100)/100
            listesayici.append(rakamlar[int(b-1)])
            listesayici.append("hundred")
            c=a%10
            c=a-c
            c=(c%100)/10
            d=a%10
            if(c!=0 or d!=0):
                listesayici.append("and")
            if(c==1):
                    if(d==1):
                        listesayici.append("eleven")
                    elif(d==2):
                        listesayici.append("twelve")
                    elif(d==3):
                        listesayici.append("thirteen")
                    elif(d==4):
                        listesayici.append("fourtenn")
                    elif(d==5):
                        listesayici.append("fifteen")
                    elif(d==6):
                        listesayici.append("sixteen")
                    elif(d==7):
                        listesayici.append("seventeen")              
                    elif(d==8):
                        listesayici.append("eighteen")                    
                    elif(d==9):
                        listesayici.append("nineteen")
                    elif(d==0):
                        listesayici.append("ten")
    if(len(kstring)==2):
        if(kstring[-2]!="1"):
            c=a%10
            c=a-c
            c=(c%100)/10
            d=a%10
            if(c!=0):
                listesayici.append(onlar[int(c-1)])
            if(d!=0):
                listesayici.append(rakamlar[int(d-1)])
        else:

            c=a%10
            c=a-c
            c=(c%100)/10
            d=a%10
            if(c==1):
                    if(d==1):
                        listesayici.append("eleven")
                    elif(d==2):
                        listesayici.append("twelve")
                    elif(d==3):
                        listesayici.append("thirteen")
                    elif(d==4):
                        listesayici.append("fourtenn")
                    elif(d==5):
                        listesayici.append("fifteen")
                    elif(d==6):
                        listesayici.append("sixteen")
                    elif(d==7):
                        listesayici.append("seventeen")              
                    elif(d==8):
                        listesayici.append("eighteen")                    
                    elif(d==9):
                        listesayici.append("nineteen")
                    elif(d==0):
                        listesayici.append("ten")
    if(len(kstring)==1):
        listesayici.append(rakamlar[i-1])
harfsayisi=0
for i in listesayici:
    harfsayisi+=len(i)
                    
