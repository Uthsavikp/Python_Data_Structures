''' 
@Author: Uthsavi KP
@Date: 2021-01-05 14:42:36
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 15:56:53
@Title: To Remove An Item From Tuple  
'''

class RemoveItem:
    def __init__(self):
        pass
    def remove_item_from_tuple(self):
        """
        removing an item from tuple
        """
        tuple_elements = (3,43,65,21,89,0)
        list_elements = list(tuple_elements)
        list_elements.pop(3)
        tuple_elements = tuple(list_elements)
        print("After removing items")
        print(tuple_elements)

if __name__ == "__main__":
    removeitem = RemoveItem()
    removeitem.remove_item_from_tuple()