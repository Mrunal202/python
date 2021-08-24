# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 07:40:31 2021

@author: hp
"""
# formatting of printnig strings 
name="mrunal"
age=30
print("my age is %d"%(age))
print("my age is {}".format(age))

#positional
print("my name is {} and my age is {}".format("shriyan",1))
print("my name is {} and my age is {}".format(age,name))
#keywors based
print("my name is {name1} and my age is {age1}".format(name1=name,age1=age))