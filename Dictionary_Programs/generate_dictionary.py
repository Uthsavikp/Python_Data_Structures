''' 
  @Author: Uthsavi KP
  @Date: 2021-01-07 23:46:23
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-07 23:46:23
  @Title: To generate a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
'''

class GenerateDictionary:
    def __init__(self):
        pass
    def get_dictionary(self):
        """
        generating dictionary which contains a number (between 1 and n)
        """
        number = int(input("Enter a number : "))
        print("dictionary :",{variable : variable*variable for variable in range(1,(number+1))})

if __name__ == "__main__":
    generating = GenerateDictionary()
    generating.get_dictionary()