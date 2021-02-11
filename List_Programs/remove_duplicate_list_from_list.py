''' 
  @Author: Uthsavi KP
  @Date: 2021-01-05 18:28:19
  @Last Modified by:   Uthsavi KP
  @Last Modified time: 2021-01-05 19:02:43  
  @Title: To remove duplicates from a list of lists.
'''

class DuplicateList:
    def __init__(self):
        pass
    def remove_duplicate(self):
        """
        removing duplicates from a list 
        """
        list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        new_list = []
        for elements in list1:
            if elements not in new_list:
                new_list.append(elements)
        print("New list without duplicates")        
        print(new_list)

if __name__ == "__main__":
    duplicatelist = DuplicateList()
    duplicatelist.remove_duplicate()                