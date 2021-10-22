# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 03:15:41 2021

@author: HP
"""

import pandas as pd
import os
os.getcwd()
df=pd.read_csv('Untitled Folder\developer_survey_2019\survey_results_schema.csv')
df[0:6]


dict1={"name":["mrunal","rajat","Shriyan"]
       ,"rollno":[1,2,3]}
list1=[1,2,3,5,6]
myvar = pd.DataFrame(dict1)

print(myvar)

a=[1,2,3,425]
b=(23)
s={1,256,44}
v1=pd.Series(s)
print(v1)

m1=pd.Series(a,index=[5,6,7,8])

print(m1[8])
dict2={1:"a",2:"b",3:"c"}
myvar2=pd.Series(dict2)
print(myvar2)
myvar3=(pd.Series(dict2,index=[1,2]))
print(myvar3)

print(myvar2.transpose)


myvar2[0:1]

myvar2.loc[3]



data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
print(myvar.loc[[0,1]])

myvar.loc[0:3,'calories']
myvar.loc[0:3,['calories','duration']]
myvar=myvar['calories']
myvar
print(myvar.iloc[0:2,1:3])



import os
os.getcwd()


import pandas as pd

df=pd.read_csv("mrunal.csv")
print(df.to_string())




import pandas as pd

df = pd.read_json("mrunal1.json")

print(df.to_string()) 




import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 