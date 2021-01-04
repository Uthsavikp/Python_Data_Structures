'''
* @Author: Uthsavi KP
* @Date: 2020-01-04 13:20:33 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-04 13:20:33
* @Title : To print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
'''

def unique_colour():
    color_list_1 = set(["White", "Black", "Red"]) 
    color_list_2 = set(["Red", "Green"])

    print(color_list_1.difference(color_list_2))
unique_colour()    