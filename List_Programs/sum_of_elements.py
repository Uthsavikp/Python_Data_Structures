''' 
  @Author: Uthsavi KP
  @Date: 2021-01-05 02:14:53
  @Last Modified by:   Uthsavi KP
  @Last Modified time: 2021-01-05 03:43:47  
  @Title: To Count The Strings Inside List.
''' 
class SumOfElements:
    def __init__(self):
        self.list1 = [] 
    
    def calculate_sum(self):
        """
        getting the sum of all elements
        """
        list_number = int(input("Number of elements :"))
        for _ in range(list_number):
            list_elements = int(input("Enter the element :"))
            self.list1.append(list_elements)    
        print("Sum Of All The Elements In List Is :", sum(self.list1))
        
if __name__ == "__main__":
  
    total = SumOfElements()
    total.calculate_sum()