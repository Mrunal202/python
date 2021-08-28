# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 21:17:06 2021

@author: HP
"""

dict={}print(len(dict1))
print(dict)

dict1={
      1:"name",
      2:"address",
      3:"phonenumber",
      "abc":"xyz"
      }

print("dictionary is:",dict1)

print(type(dict1))
print(len(dict1))

print("value at 1 is :",dict1[1])

print("value at abc is :",dict1["abc"])

print("all values of dictionary are:",dict1.values())
print("all keys of dictionary are:",dict1.keys())

list1=[10,20,30,40,50,60]
list2=['a','b','c','d','e','f']


dict2=dict.fromkeys(list1)
print(dict2)

print(dict.fromkeys(list1,"python"))

print(dict2.fromkeys(list1,list2))


dict2.update({10:"A" ,20:"B",70:"Z"})

print(dict2)

dict3=dict2.copy()
print(dict3)


print(dict3.get(10))


print(dict3.pop(20))

print(dict3.popitem())

print(dict3.items())

print(dict3.setdefault(55))










