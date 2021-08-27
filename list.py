# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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



list4=[1,2,5,6]

#finding min max
print(max(list4))
print(min(list4))

#concatenation
list5=list1+list4
print(list5)


#in not in operator
print("1 in list1",1 in list1)
print("3 in list4",3 not in list4)
print(list4*2)


#append  ans extend
list7=[11,56,78]
list7.append(25)
print(list7)

list7.extend("abc")
print(list7)

list7.extend(["abc","xyz"])
print(list7)

list2.append(22)
print(list2)

list1.append(list2)
print(list1)
print(list1*1)

list1.extend(list2)
print(list1)

print(list1[7][2])

print(len(list1))

list2.extend([1,2,3])
print(list2)

list2[7]=89
print(list2)

list2[2:4]=20,"mrunal"
print(list2)





list2[2]=55
print(list2)

l={'p':1}
list2.append(l)
list2.extend(l)
print(list2)


#insert

print(list4)
list4.insert(1,55)
list4.insert(0,36)
list4.insert(2,89)
list4.insert(3,95)
list4.sort()


#index
print("index of 89 is:",list4.index(89))
print("length of list 4:",len(list4))

list4.append(5)
list4.append(5)


#count
print("count of 5 is",list4.count(5))
print("count of 89 is",list4.count(89))


#pop and remove

list4.remove(95)
list4.remove()

list4.pop()
list4.pop(2)

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