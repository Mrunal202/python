# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 07:10:21 2021

@author: HP
"""
#without arguments
def concatinate():

    name="mrunal"
    surname="vaidya"
    return name+surname

res=concatinate()
print("full name is",res)

#with arguments
def concatinate1(name,last):
    return name+last

res=concatinate1("mrunal","vaidya")
print("full name is:",res)


#without arguments
def concat1():
    name="mrunal"
    surname="vaidya"
    return type(name),surname

res=concat1()
print(res)



def concat2():
    name="mrunal"
    surname="vaidya"
    print(name,surname)
    
concat2()

#without arguments
def list_create():
    l1=[10,20,30,40]
    print("list1 is created",l1)
    return l1

res=list_create()



def list_append():
    l1=[20,30,45]
    l1.append(88)
    print("list is",l1)
    return l1

list_append()




#with arguments

def new_list(list1):

    print("list created")
    return list1

list1=[10,20,50,66]
print("new list is",new_list(list1))


def List_append(list1,n):
    list1.append(n)
    return list1

#list1=[10,52,89,63]
#n=99

print("new list added is:",List_append([22,33,88],99))


#addition of two numbers
def add1(a,b):
    return a+b

a=int(input("enter first number"))
b=int(input("enter second number"))
print("addition is",add1(a,b))

#area of circle
def areaofc(r):
    p=3.14
    return p*r*r

r=int(input("enter the radius of circle"))
print("area of circle is",areaofc(r))


#dictionary update
def dictupdate(d1):
    d1.update({"d":4})
    print("keys are:",d1.keys())
    print("values are:",d1.values())
    return d1
 

d1={"a":1,"b":2,"c":3}
print("dictionary is ",dictupdate(d1))   
#sum of n numbers

def sumofn():
    n=int(input("Enter the number range:"))
    sum=0
    for i in range(0,n+1):
        sum=sum+i
    return sum
    
print("sum of a numbers is",sumofn())



#sum of numbers from list
def sumlist(l1):
    sum=0
    l2=l1.copy();
    print(l2)
    for i in range (0,len(l1)):
        sum=sum+l1[i]
    return sum


l1=[1,2,3,4]
print("Sum of list elements is",sumlist(l1))

