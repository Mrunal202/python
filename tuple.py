# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 20:56:18 2021

@author: HP
"""

a=()    #empty tuple
a=(10)  #this is int
a=(10,)  #single valued tuple

#define tuple
a=(5,1,6,5,1,"python",60)
print("length of tuple us",len(a))   #length 


print("Type of A is:",type(a))    #type

print("count of 1 in tuple is:",a.count(1))   #count

print("index of python is :",a.index("python"))   #index
a.index(5)


#addition of list and dictionary at he time of creartion only
b=(10,[20,"a",10],{1:'a'})
b[1][2]=50     #updation of list is allowed
b[0]=66      #updation of tuple is not allowed 


#del(a)

'''
a.index(5)
Traceback (most recent call last):

  File "<ipython-input-15-d81d2b00d317>", line 1, in <module>
    a.index(5)

NameError: name 'a' is not defined'''