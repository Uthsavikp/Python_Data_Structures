'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 01:15:06 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 01:26:48
* @Title : To get file creation and modification date/times. 
'''

import os
import datetime
 
file = r"C:\Users\uthsa\week-2_data_structures\Basic_Python\reverse_order.py"
 
print("Created")
print(os.path.getctime(file))
print(datetime.datetime.fromtimestamp(os.path.getctime(file)))
 
print()
 
print("Modified")
print(os.path.getmtime(file))
print(datetime.datetime.fromtimestamp(os.path.getmtime(file)))