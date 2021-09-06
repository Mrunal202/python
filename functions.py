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


    