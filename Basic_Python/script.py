'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 2:12:58 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 2:33:09
* @Title : To pass the arguments into script.
'''
import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))