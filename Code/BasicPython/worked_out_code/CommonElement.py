# -*- coding: utf-8 -*-
"""
Q. To create list of common elements in two lists
"""

list1=list(input("list 1 is:"))
list2=[int(i) for i in list1]
list3=list(input("list 2 is:"))
list4=[int(i) for i in list3]
s1= set(list2)
s2= set(list4)
print(list(s1.intersection(s2)))

