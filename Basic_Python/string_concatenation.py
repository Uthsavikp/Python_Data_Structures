'''
* @Author: Uthsavi KP
* @Date: 2020-01-04 13:02:19  
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-04 13:02:19
* @Title : Program to concatenate all elements in a list into a string and return it.
'''

def concatenate():
    list_elements = ["Hello","how","are","you","?"]
    string = ""
    for elements in list_elements:
        string = string +" "+ elements #concatenating to get the output in string formate
    print(string)

concatenate()
