# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:23:58 2022

@author: user
"""

for i in range (1,51):
    if i >=34 and i <=41:
        continue
    if i %3 == 0 and i%5==0:
        print (i, "well done")
    elif i % 3 == 0 :
        print (i,"well")
    elif i % 5 == 0 :
        print (i,"done")
    for i in range (34,42):
        continue