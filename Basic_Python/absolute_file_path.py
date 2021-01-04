'''
* @Author: Uthsavi KP
* @Date: 2020-01-04 14:56:16 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-04 4:56:16 
* @Title : Program to get absolute file path.

'''

import os
def absolute_file_path(path_name):
    return os.path.abspath("path_name")
print("Absolute path: ",absolute_file_path("current_username.py"))    