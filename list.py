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







#slicing of list 
print("Printing list [1:4]",list1[1:4])   #   [2, 3, 'A']


#whole list
print( "Printing list [:]",list1[:])  #[1, 2, 3, 'A', 'mrunal']

#with interval of 2 
print("Printing list [::2]",list1[::2])   #[1, 3, 'mrunal']


#with interval of 3
print("Printing list [::3]",list1[::3]) #   [1, 'A']



list2=[5,6,9,'xyz','python',10.5,59]


print("list2 is:",list2)
print("type of list2 is:",type(list2))
print("length of list2:",len(list2))


print(list2[-1:-5:-1])  #[59, 10.5, 'python', 'xyz']
list2[-2:3:-1]   #   [10.5, 'python']

#reverse
print("reverse of list is",list1[::-1])
list1.reverse()





list2.append(22)
print(list2)

list2[7]=89
print(list2)

list2[2:4]=20,"mrunal"
print(list2)

list2.insert(4, """cpp""")
print(list2)
list2.remove("cpp")
print(list2)

list2.pop(6)
print(list2)



list2[2]=55
print(list2)

'''' to check given element in list'''

if 58 in list2:
    print("yes")
else:
    print("no")
    
#extend
list3=[10]
list3.extend(list2)
print(list3)



#print using for
for x in list2:
    print(x)

#print using while

i=0
while i<len(list3):
    print(list3[i])
    i=i+1
    
    
    
list2.count(89)
list2.__contains__(89)
