'''
* @Author: Uthsavi KP
* @Date: 2020-01-04 15:36:03 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-04 15:36:03 
* @Title : To print the calendar of a given month and year.

'''

import calendar #importing calendar module
month_input = int(input("Enter month: "))
year = int(input("Enter year: "))
    
# display the calendar  
print(calendar.month(year,month_input))     