''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 20:11:13
  @Last Modified by:   Uthsavi KP
  @Last Modified time: 2021-01-05 20:58:33  
  @Title: To get the smallest number from a list.
'''

class Smallest:
    def __init__(self):
        pass
    def smallest_value(self):
        """
        getting the smallest number
        """
        small = []
        number = int(input("Enter the list length : "))
        for _ in range(number):
            elements = int(input("Enter the elements : "))
            small.append(elements)
        print("Smallest number is : ", min(small))    

if __name__ == "__main__":
    smallest = Smallest()
    smallest.smallest_value()        