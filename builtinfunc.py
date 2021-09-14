# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 06:12:16 2021

@author: HP
"""

import os
print(os.getcwd())

import os
os.mkdir("C:\\Users\\HP\\newfolder1")


import os
os.chdir("C:\\Users\\HP\\newfolder")
print(os.getcwd())
os.chdir("C:\\")
print(os.getcwd())
print(os.chdir("C:\\Users\\HP"))


print(os.chdir(".."))

os.rmdir("C:\\Users\\HP\\newfolder\\")
os.listdir("C:\\Users\\HP")
os.listdir()

import sys
print(sys.path)


sys.version