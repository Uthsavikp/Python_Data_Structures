'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 2:12:58 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 2:33:09
* @Title : To get system command output.
'''

import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)