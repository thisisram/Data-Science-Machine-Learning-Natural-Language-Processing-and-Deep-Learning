# -*- coding: utf-8 -*-
"""
Q. To print all the elements of nested loops by iterating with for loops
"""

country=['US','japan','India',['Maharashtra','Delhi',['pune','solapur','karad'],'Kerala']]

def ListInList(list_1, level):
    for i in list_1:
        if isinstance(i,list):
             
             ListInList(i,level+1)
        else:
            for tabs in range(level):   
              print("\t",end=" ")
            print(i)
     
ListInList(country,0)        
    