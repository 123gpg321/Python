# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:47:28 2017

@author: Shubham Purohit
"""

n=input("Enter a value(>0):")

if n<1:                                 # Check if number of rows > 0
    pass
else:
    print [1]                           #print first row
    l=[1,1]                            # reference string 
    for i in range(1,n):
        k=[1,1]                         # initialize output list
        for j in range(1,i):
            k.insert(j,(l[j-1]+l[j]))   # update output list
        print k                          # print consequent rows  
        l=k
        
            
            
        
    