'''
* @Author: Uthsavi KP
* @Date: 2020-01-04 13:33:09 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-04 13:33:09
* @Title : To Print The User Input In Reverse Order With A Space Between Them
'''

def reverse_name():
    first_name = input("enter first name:")
    last_name = input("Enter last name:")
    name = first_name + " "  + last_name # to concatenate  user input with a space in between
    print(name[::-1]) #prining the result in reverse order
reverse_name()    