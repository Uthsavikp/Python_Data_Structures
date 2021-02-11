''' 
  @Author: Uthsavi KP
  @Date: 2021-01-08 20:34:29
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-08 20:47:03
  @Title: To reverse the order of the items in the array.
'''

class ReverseArray:
    def get_reversed_array(self):
        my_array = []
        for _ in range(int(input("Enter number of elements : "))):
            my_array.append(int(input("Enter array elements : ")))
        print("Original array :", my_array)    

        reversed_array = my_array[::-1]
        print("Reversed array :",reversed_array)

if __name__ == "__main__":
    reverse_array = ReverseArray()
    reverse_array.get_reversed_array()        