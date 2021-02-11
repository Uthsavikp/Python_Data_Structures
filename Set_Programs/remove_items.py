''' 
@Author: Uthsavi KP
@Date: 2021-01-05 08:25:53
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 08:25:53
@Title: To Remove Items From A Set  
'''

class RemoveItems:
    
    def revome_item_from_set(self):
        """
        remove items from a set
        """
        set_elements = {'45','set','a','you','2','24'}
        set_elements.remove('a')
        print(set_elements)

if __name__ == "__main__":
    remove_itm = RemoveItems()
    remove_itm.revome_item_from_set() 