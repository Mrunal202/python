# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 06:22:27 2021

@author: HP
"""

import pandas as pd
import numpy as np


####SERIES####
l1=[1,2,3,4,5]
l2=["a","b","c","d","e"]
mydata=pd.Series(l1,l2)
print(mydata)
mydata.loc[0:3,1]
type(l1)
type(mydata)


date=pd.date_range("20160623",periods=7)
print(date)

df=pd.DataFrame(np.random.randn(7,4),index=date,columns=list('ABCD'))
print(df)


dict1={"Name":["a","b","c"],"Age":[90,20,50]}
m1=pd.DataFrame(dict1,index=(1,5,3))
print(m1)


print(m1.head(1))
print(m1.tail(2))
print(m1.describe())
print(m1.sort_index(axis=1))
print(m1.sort_index(axis=0))
print(m1.sort_values(by="Age",ascending="False"))
m1.transpose()
