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


#swapping numbers fron list
def swaplist(list1):
    temp=list1[0]
    list1[0]=list1[-1]
    list1[-1]=temp
    return list1

list1=[10,20,30,45]
print("list after swapping is:",swaplist(list1))


def swaplist(list1):
    for i in range(0,len(list1)-1):
         # temp=list1[i]
       # list1[i]=list1[i-1]
        #list1[i-1]=temp
        list1[i],list1[-1-i]=list1[-1-i],list1[i]
    
    return list1

list1=[10,20,30,45,60]
print("list after swapping is:",swaplist(list1))



###############SWAPPING WITH POSITIONS

def swappos(list1,pos1,pos2):
    list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
    return list1

list1=[10,20,30,40]
pos1=int(input("Enter position1"))
pos2=int(input("enter position2"))
print("after swapping elements list1 is:",swappos(list1,pos1,pos2))


####reversing the words
sen="mrunal vaidya"
words=sen.split(" ")
words=list(reversed(words))
print("".join(words))
print(words)

#random number from list
import random
list1=[1,2,3,5,6]
print(random.choice(list1))


#enumerator
list1=["apple","banana","orange"]
enum1=enumerate(list1)
print(list(enum1))

for j in enumerate(list1):
    print(list(j))
type(enumerate(list1))

for count,item in enumerate(list1,100):
    print(count,item)
    
    
    
    
    #addition of two numbers
def add1(a,b):
    return a+b

a=int(input("enter first number"))
b=int(input("enter second number"))
print("addition is",add1(a,b))

 ##################LAMBDA FUNCTION#############
 ###addition
sum1 =lambda x,y: x+y
x=int(input("enter the value1:"))
y=int(input("enter the value2:"))
print(sum1(x,y))

##area
area1=lambda r: 3.14*r*r
r=int(input("enter radius:"))
print("area of circle is",area1(r)) 

##square
import math
def square(n):
    return math.pow(n, 2)

print("square is:",square(5))

square1=lambda n: n**2
print("square is:",square1(10))
type(square1)


def add3(x,y,z):
    return x+y+z

print("addition is",add3(10,40,50))

add3=lambda x,y,z: x+y+z
print("addition is",add3(3,3,1))



######MAP FUNCTION####
sqr= map(lambda x:x*x,list1)
list1=[10,20,30]
type(sqr)
print("square is",list(sqr))

sqr1=map(lambda x:x*x,d1.values())
d1={"a":1,"b":2}
print("square is",list(sqr1))



L=[lambda x:x*x,lambda x:x*x*x, lambda x:x*x*x*x*x]
for f in L:
    p=f(4)
    print(p)
    
    
    
    
list1=[10,20,30,40]
list2=[10,20,30,40]

p=map(lambda x,y:x+y ,list1,list2)
print(list(p))


t1=(1,2,3,4)
t2=(4,5,6,7,8)
mul=map(lambda x,y:x+y-x,t1,t2)
print(tuple(mul))



#FILTER FUNCTION#######

list1=[10,50,49,85,65,15,21,32,9]
result=filter(lambda x: x>50,list1)
print(list(result))

result1=filter(lambda x: x%2==0 or x%5==0 ,list1)
print(list(result1))

numlist=range(-10,2)
lessthanzero=filter(lambda x: x<0,numlist)
print(list(lessthanzero))

########reduce

from functools import reduce
f=lambda a,b:a if (a>b ) else b
print(reduce(f,[1,5,9,8,100,56]))
