'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 04:33:19 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 04:45:02
* @Title : To list all files in a directory.
'''

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir(r'C:\Users\uthsa\week-2_data_structures\Basic_Python') if isfile(join(r'C:\Users\uthsa\week-2_data_structures\Basic_Python', f))]
print(files_list)