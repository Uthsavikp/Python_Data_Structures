'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 01:42:19 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 2:00:18
* @Title : To Sort Files By Date.
'''
import glob
import os

files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))