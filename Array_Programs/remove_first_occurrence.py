''' 
  @Author: Uthsavi KP
  @Date: 2021-01-08 18:02:24
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-08 18:45:26
  @Title: To remove the first occurrence of a specified element from an array.
'''

class RemoveElement:
    def remove_first_occurance(self):
        """
        removing the first occurance of a specified element  
        """
        my_array = []

        try:
            for _ in range(int(input("Enter the number : "))):
                my_array.append(int(input("Enter the array elements : "))) 
            print("Array elements :",my_array)
            my_array.remove(int(input("Enter the number you want to count : "))) 
            print("Array after removal of an element :",my_array)    
        except Exception as err:
            print(err)

if __name__ == "__main__":
    remove_element = RemoveElement()
    remove_element.remove_first_occurance()
