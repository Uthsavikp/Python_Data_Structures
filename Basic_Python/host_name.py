'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 2:46:47 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 2:50:09
* @Title : To get the name of the host on which the routine is running. 
'''

import socket
host_name = socket.gethostname()
print()
print("Host Name:", host_name)
print()