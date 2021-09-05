# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 05:59:40 2021

@author: HP
"""

p={1,2,3}
p.add(50)
p.add(55)
print(p)
d={"a":10,"b":20,"c":30}
s=set(d)

s.add(56)
s.add("n")
print(s)

s.remove("b")

s.pop()

s.clear()
print(s)





s1=(100,24,56,78,99)
s2=(45,67,89,99)
s33={45,99}
s11=set(s1)
s22=set(s2)
print("set 1 is :",s11)
print("set 2 is ",s22)
print("intersection is:",s11&s22)
print("union is:",s11|s22)
print("symmetric difference is:",s11.symmetric_difference(s22))
print("diference is:",s11-s22)
print("s11>=s22",s11>=s22)
print("s11<=s22",s11<=s22)
print(s33.issubset(s22))
print(s22.issuperset(s33))
s11.isdisjoint(s22)

s11.update(s22)
s11.update(s2)

