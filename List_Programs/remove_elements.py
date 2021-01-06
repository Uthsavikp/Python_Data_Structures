''' 
  @Author: Uthsavi KP
  @Date: 2021-01-05 14:42:05
  @Last Modified by:   Uthsavi KP
  @Last Modified time: 2021-01-05 16:08:35  
  @Title: To print list after removing the 0th, 4th and 5th elements.
'''

class RemoveElements:
    def __init__(self):
        pass
    def elements_removal(self):
        """
        removing elemets from the list
        """
        given_list =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        del given_list[0]
        given_list.remove('Pink')
        given_list.pop() #pop removes elements from the end
        print("Elements remaining: ", given_list)
if __name__ == "__main__":
    removal = RemoveElements()
    removal.elements_removal()        