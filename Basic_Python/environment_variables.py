'''
* @Author: Uthsavi KP
* @Date: 2020-01-04 14:28:56 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-04 4:28:56 
* @Title : Program to access environment variables

'''
import os

print(os.environ)
print("*"*20)
print(os.environ['HOME'])
print("*"*20)
print(os.environ['PATH'])