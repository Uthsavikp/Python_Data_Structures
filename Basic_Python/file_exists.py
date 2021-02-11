'''
* @Author: Uthsavi KP
* @Date: 2020-01-04 13:58:03 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-04 13:58:03
* @Title : To check whether a file exists. 
'''

def file_existence():
    try:
        file = open(r"C:\Users\uthsa\Python Files\Data_Structures\check_value.py")
        print(file)
    except Exception as err:
        print("Unable to open the file:", err)
file_existence()    