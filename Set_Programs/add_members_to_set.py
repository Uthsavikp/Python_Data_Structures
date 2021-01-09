''' 
@Author: Uthsavi KP
@Date: 2021-01-05 08:25:53
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 08:25:53
@Title: To Add A New Member To Existing Set  
'''

class AddMembers:
    def add_members(self):
        """
        add memebers to a set
        """
        set_elements = {'45','set','a','you','2','24'}
        set_elements.add('so')
        print(set_elements)

if __name__ == "__main__":
    addmembers = AddMembers()
    addmembers.add_members() 