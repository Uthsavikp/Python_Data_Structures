''' 
@Author: Uthsavi KP
@Date: 2021-01-05 22:19:11
@Last Modified by: Uthsavi KP
@Last Modified time: 2021-01-06 02:32:26 
@Title: To Remove Item If It Is Present 
'''

class Remove:
    def __init__(self):
        pass
    def revome_if_present(self):
        """
        remove item if present in a set
        """
        set_elements = {'45','set','data',24,87,'enjoy','2','24'}
        if 'enjoy' in set_elements: #checking if the element is present
            set_elements.remove('enjoy')
        print(set_elements)

if __name__ == "__main__":
    remove = Remove()
    remove.revome_if_present() 