''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 23:27:24
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-06 23:57:31
  @Title: To multiply list elements.
'''
 
class Multiplication:
    def __init__(self):
        pass

    def multiply_list_elements(self,list1,list2):
        """
        multiplying all the elements 
        """
        multiplication_list = []
        for number1, number2 in zip(list1,list2):
            multiplication_list.append(number1*number2)
        print("Product of list1 and list2 : ",multiplication_list)    

if __name__ == "__main__":
    multiply = Multiplication()
    multiply.multiply_list_elements([2,4,9,10],[1,5,14,2])  