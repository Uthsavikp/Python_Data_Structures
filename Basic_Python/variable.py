'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 3:12:19 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 3:20:09
* @Title : To find if a variable is defined or not.
'''

try:
  number = 1
except NameError:
  print("Variable is not defined")
else:
  print("Variable is defined")
try:
  element
except NameError:
  print("Variable is not defined")
else:
  print("Variable is defined.")