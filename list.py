# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 05:56:46 2021

@author: Rajat
"""
list1=[1,2,3,'A','mrunal']
print("list1 is:",list1)
len(list1)
type(list1)


print("type of list1 is:",type(list1))


list2=[5,6,9,'xyz','python']


print("list2 is:",list2)
print("type of list2 is:",type(list2))
print("length of list2:",len(list2))




#slicing of list 
print("Printing list [1:4]",list1[1:4])   #   [2, 3, 'A']


#whole list
print( "Printing list [:]",list1[:])  #[1, 2, 3, 'A', 'mrunal']

#with interval of 2 
print("Printing list [::2]",list1[::2])   #[1, 3, 'mrunal']


#with interval of 3
print("Printing list [::3]",list1[::3]) #   [1, 'A']



#reverse
print("reverse of list is",list1[::-1])
list1.reverse()

list1.append(22)
print(list1)

list1.remove(22)
print(list1)

list1.pop(0)
print(list1)



list1[2]=55
print(list1)
