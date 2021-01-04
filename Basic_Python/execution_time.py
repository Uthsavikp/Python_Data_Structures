'''
* @Author: Uthsavi KP
* @Date: 2020-01-04 14:12:29 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-04 4:12:29 
* @Title : To find the execution time for a python method. 
'''

import time
def execution_time():
    start_time = time.time()
    elements = [1,8,[2,3,4]]
    for numbers in elements:
        print(numbers)
    print("Execution time:",time.time() - start_time,"seconds")
execution_time()