''' 
  @Author: Uthsavi KP
  @Date: 2021-01-05 21:19:44
  @Last Modified by:   Uthsavi KP
  @Last Modified time: 2021-01-05 21:19:44  
  @Title: Program to clone or copy a list.
''' 
class Clone:

    def __init__(self):
        pass
    def copy_list(self):
        """
        cloning the list 
        """
        try:
            original_list = [1,2,"abc","22"]
            new_list = list(original_list)
            print("Original list :", original_list)   
            print("New list :", new_list)
        except Exception as err:
            print(err)
if __name__ == "__main__":
    clone = Clone()
    clone.copy_list()      