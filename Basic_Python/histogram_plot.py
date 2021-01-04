'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 04:14:16 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 04:50:09
* @Title : To create a histogram from a given list of integers. 
'''

def histogram( items ):
    for number in items:
        output = ''
        times = number
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 6, 5])