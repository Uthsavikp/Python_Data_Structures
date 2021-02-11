'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 2:12:58 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 2:33:09
* @Title : To retrieve file properties.
'''

import os.path
import time

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))
