# -*- coding: utf-8 -*-
"""
Q.Pyramid of stars like
* 
* * 
* * * 
* * * * 
* * * * * 
"""

n=int(input("Enter the no of stars:"))
for i in range(0,n):

    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
        
