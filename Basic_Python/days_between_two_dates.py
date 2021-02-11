'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 03:51:58 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 03:55:38
* @Title : To find number of days between two dates.
'''

from datetime import date
first_date = date(2020, 3, 24)
last_date = date(2021, 1, 5)
delta = last_date - first_date
print(delta.days,"Days")