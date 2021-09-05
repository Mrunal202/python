# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 21:10:57 2021

@author: HP
"""

# program for even and odd

num=int(input("enter the number:"))
if num%2==0 :
    print("number is even")
else:
    print("number is odd")
    

l1=[1,2,3,11,5,6,8,10]
for i in l1:
     if l1[i] %2==0 :
           print("number is even")
     else:
            print("number is odd")
            
            

# degree to farhenhite
c=int(input("enter the degree celcius:"))

f=(c*(9/5))+32
print("farhenhite is:",f)


#area of triangle
import math
a=int(input("enter first side:"))
b=int(input("enter second side:"))
c=int(input("enter third side:"))
if a==b==c :
    area=(a+b+c)/3
    print("area is",area)
else:
    s=(a+b+c)/2
    arr=s*(s-a)*(s-b)*(s-c)
    area1=math.sqrt(arr) 
    print("area is",area1)
     
    
 # avreage of numbers

n=int(input("enter the total numbers for which averge to be found out:"))
avg1=0
sum1=0
for i in range(0,n):
    num1=int(input("enter the number:"))
    sum1=sum1+num1
avg1=sum1/n
print("average is:",avg1)



#multiple of 5 and 7
n=int(input("enter the numbers:"))
if n%5 ==0 and n%7==0 :
    print(n,"is multiple of 5 and 7")
else:
     print(n,"is not  multiple of 5 and 7")
    

#reverse the number
x=int(input("enter the number to be reverse:"))
reverse=0
while x>0:
    rem=x%10
    reverse=(reverse*10)+rem
    x=x//10
print("reverse of a number is:",format(reverse))   
    

#pallindrome

str1=input("enter the strinf to be reversed:")
str2=str1[::-1]
print(str2)
if str2==str1:
    print("string is pallindrome")
else:
    
    print("string is not pallindrome")
    
    #factorial
n=int(input("enter the number factorial number:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1

print(fact)


#sum of 1 to 10

