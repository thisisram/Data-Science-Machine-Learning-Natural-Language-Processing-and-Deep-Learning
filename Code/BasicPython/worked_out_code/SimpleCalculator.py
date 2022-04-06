# -*- coding: utf-8 -*-
"""
Q.Simple calculator for addition and substraction
"""
def add(x, y):
   return x + y

def subtract(x, y):
   return x - y


choice=int(input("Enter a choice\n 1.Addition \n 2.Subtration\n:"))
x=int(input("First:"))
y=int(input("Second:"))
if choice==1:
    print("Answer:"+str(add(x,y)))
elif choice==2:
    print("Answer:"+str(subtract(x,y)))
else:
     pass
      
