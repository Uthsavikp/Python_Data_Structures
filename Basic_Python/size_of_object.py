'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 2:28:23 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 2:43:07
* @Title : To get size of an object.
'''

import sys
str1 = "time"
str2 = "title"
str3 = "module"
print()
print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
print()