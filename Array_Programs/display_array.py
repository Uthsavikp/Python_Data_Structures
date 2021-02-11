''' 
  @Author: Uthsavi KP
  @Date: 2021-01-08 17:27:04
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-08 17:57:42
  @Title: To create an array of 5 integers and display the array items.
'''

class DisplayArray:
    def get_array_elements(self):
        """
        creating an array of 5 integers 
        """
        my_array = []
        try:
            for _ in range(int(input("Enter the number of elements : "))):
                my_array.append(int(input("Enter the array elements : ")))
            print("Array elements are :",my_array)
        except Exception as err:
            print(err)    

if __name__ == "__main__":
    display_arr = DisplayArray()
    display_arr.get_array_elements()            