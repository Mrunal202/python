# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 04:54:22 2021

@author: HP
"""

def add1(n1,n2):
    return n1+n2

def sub1(n1,n2):
    return n1-n2

def mul1(n1,n2):
    return n1*n2

def div1(n1,n2):
    return n1//n2


n1=int(input("enter first number:"))
n2=int(input("enter second number:"))

ch=input("Enter the choice:")

if ch=="+":
    print("Addition is:",add1(n1,n2))
elif ch=="-":
    print("Substraction is:",sub1(n1,n2))
elif ch=="*":
    print("Multiolication is",mul1(n1,n2))
elif ch=="/":
    print("Division is ",div1(n1,n2))
else:
    pass