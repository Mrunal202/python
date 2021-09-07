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
    
    
    ###
    str1=input("enter the string:")
    half=int(len(str1)/2)
    print(half)
    str2=str1[0:half]
   
    str3=str1[half:]
   
    if str2==str3:
        print("string is symmetrical")
    else:
        print("string is not symmetrical")
    
    
 #####sum of tuple elements
t1=(1,2,3,5,4,6,7,8,9)
print(len(t1))   
sum1=0
for i in range(0,len(t1)):
    sum1=sum1+t1[i]
    i=i+1

print(sum1)



####sum of a digit###

n=int(input("enter the number:"))
sum1=0
while n!=0:
    
    sum1=sum1+(n%10)
    n=n//10
print(sum1)

for i in range (100,200):
    num=i
    sum1=0
    while num!=0:
        sum1=sum1+(n%10)
        num=num//10
    if (sum1%2 ==0):
        print(i)

for i in range(100,200):
    num = i
    sum = 0
    while(num!=0):
        digit = num%10
        sum = sum + digit
        num = num//10
    if(sum%2==0):
        print(i)
    
    
    #factorial
n=int(input("enter the number factorial number:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1

print(fact)


###prime number
n=int(input("enter the number:"))
if n>1:
    for i in range (2,n):
        if n%i ==0:
            print("number is not a prime number:")
            break
    else:
            print("number is a prime number")
else:
    print("number is not prime")


num =int(input("Enter the range: "))
for n in range(1,num):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n)   


##########date time
import datetime
ct=datetime.datetime.now()
print(ct)
ct=datetime.date(2021, 9, 6)
print(ct)



import datetime
today=datetime.datetime.today()
print("today is ",today)
ct1=datetime.datetime.now()
print("year is",ct1.year)
print("month is",ct1.month)
print("day is",ct1.day)
print("time is hour",ct1.hour)
print("time in min",ct1.minute)
print("time in second",ct1.second)
print("time in ms is",ct1.microsecond)

