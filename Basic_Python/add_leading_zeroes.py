'''
* @Author: Uthsavi KP
* @Date: 2020-01-06 12:04:52 
* @Last Modified by: Uthsavi KP
* @Last Modified time: 2020-01-06 12:04:52
* @Title : To add leading zeroes to a string.
'''

class AddLeadingZeroes:
    def leading_zeroes_to_string(self):
        """
        adding leading zeroes to string
        """
        print("Added leading zeros:")
        str1='122.22'
        str1 = str1.rjust(8, '0')
        print(str1)
        str1 = str1.rjust(10, '0')
        print(str1)

if __name__ == "__main__":
    leading_zeroes = AddLeadingZeroes()        
    leading_zeroes.leading_zeroes_to_string()