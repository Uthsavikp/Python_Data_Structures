'''
* @Author: Uthsavi KP
* @Date: 2020-01-06 22:57:10 
* @Last Modified by: Uthsavi KP
* @Last Modified time: 2020-01-06 22:57:10
* @Title: To determine if the python shell is executing in 32bit or 64bit mode on operating system. 
'''
import struct
class CheckMode:
    def check_mode_on_operating_system(self):
        """
        For 32 bit it will return 32 and for 64 bit it will return 64
        """
        print(struct.calcsize("P") * 8)

if __name__ == "__main__":
    check_mode = CheckMode()
    check_mode.check_mode_on_operating_system()        