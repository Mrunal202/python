# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 05:28:52 2021

@author: HP
"""

#Write a program to create a function that takes two arguments, name and age, and print their value.

def nameage(name,age):
     print("Name is: ",name,"Age is:",age)
    
name=input("Enter the name:")
age=int(input("Enter the age:"))
nameage(name,age)
    

#Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. 
def cal(a,b):
    print("Addition is:",a+b)
    print("Substraction is:",a-b)
    
a=int(input("Enter a:"))
b=int(input("Enter b:"))
cal(a,b)



#Write a program to create a function show_employee() using the following conditions.

#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name,sal=9000):
  
 print("Name is:",name,"Salary is:",sal)
 
  
    
     

name=input("Enter the name:")
sal=int(input("Enter the sal:")) 
name1= input("Enter the name:")

show_employee(name,sal)
show_employee(name1)

#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

def sumofno():
    sum1=0
    for i in range(0,10):
        sum1=sum1+i
        return sum1
  
      
print("Sum is:",sumofno())

def func(num):
    if num:
        return num + func(num-1)
    else:
        return 0
func(10)

#Generate a Python list of all the even numbers between 4 to 30
l1=[]
for i in range(4,30):
    if i%2==0:
        l1.append(i)
    else:
        pass
print(l1)

#Find the largest item from a given list
li=[1,99,88,77,12,56,9,36]
print(max(li))


 #Write a program to create function func1() to accept a variable length of arguments and print their value.
def func1(*args):
    print (*args)
  
func1("mrunal",1,"raj")
     