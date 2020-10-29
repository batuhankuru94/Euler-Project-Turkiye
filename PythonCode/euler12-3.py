#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:38:42 2020

@author: batuhankuru
"""

def  pbss(x):
    carp=1;
    top=0;
    z=2
    liste=[];
    while(x!=1):
        if(x%z==0):
            liste.append(z);
            x=x/z;
        else:
            z+=1;
    listesayici=0;
    counter=0
    depo=0
    while(len(liste)>0):
        depo=liste[0];
        for i in range(0,len(liste)):
            if(depo==liste[i]):
                counter+=1;
        carp=carp*(counter+1);
        for i in range(len(liste)-1,-1,-1):
            if(liste[i]%depo==0):
                del liste[i];
        counter=0;
        
    print(carp);
    print(liste);
