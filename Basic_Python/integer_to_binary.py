'''
* @Author: Uthsavi KP
* @Date: 2020-01-06 20:46:32 
* @Last Modified by: Uthsavi KP
* @Last Modified time: 2020-01-06 20:46:32
* @Title: To convert an integer to binary keep leading zeros. 
'''

class IntegerToBinary:
    def to_binary_with_leading_zeroes(self):
        """
        converting an integer to binary keep leading zeros
        """
        number = 50
        print(format(number, '010b'))
        print(format(number, '012b'))

if __name__ == "__main__":
    int_to_binary = IntegerToBinary()
    int_to_binary.to_binary_with_leading_zeroes()      