'''
* @Author: Uthsavi KP
* @Date: 2020-01-04 13:46:14 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-04 13:46:14
* @Title : To accept comma-separated numbers from user and generate a list and a tuple with those numbers.  
'''

values = input("Enter comma separated numbers:")
list_conversion = values.split(",")
tuple_conversion = tuple(list_conversion)
print("List: ", list_conversion)
print("tuple: ", tuple_conversion)
