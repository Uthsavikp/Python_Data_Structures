''' 
  @Author: Uthsavi KP
  @Date: 2021-01-05 18:28:19
  @Last Modified by:   Uthsavi KP
  @Last Modified time: 2021-01-05 19:02:43  
  @Title: To find common items from two lists.
'''
class CommonItems:
    def __init__(self):
        pass
    def common_items(self,list1,list2):
        """
        using list comprehension 
        to find common items
        """
        common_list = [value for value in list1 if value in list2]
        print("Common elements from both lists")
        print(common_list)

if __name__ == "__main__":
    common = CommonItems()
    common.common_items(["23",87,77,93,"blank","space"],["blank",77,1,81,32,"space"])        