'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 3:15:41 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 23:28:10
* @Title : To get numbers divisible by fifteen from a list using an anonymous function. 
'''

num_list = [45, 55, 60, 37, 100, 105, 220]
# use anonymous function to filter
result = list(filter(lambda number: (number % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)
 