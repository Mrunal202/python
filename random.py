# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 05:38:58 2021

@author: HP
"""

import random
print(random.random)

random.randint(1,4)
random.randint(-99,-1)

random.randrange(1,100,5)
random.randrange(0,10,2)

li=[1,2,5,6,89,78]
random.choice(li)

random.choice("computer")


random.shuffle(li)
print(li)
