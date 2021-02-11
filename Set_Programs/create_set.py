''' 
@Author: Uthsavi KP
@Date: 2021-01-05 20:44:21
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-06 01:25:53
@Title: To Create A New Set. 
'''

class CreateSet:
    def create_a_set(self):
        """
        creating a set
        """
    try:
        set_elements = set(input("Enter set elements: "))
        print(set_elements)
    except Exception as err:
        print("Invalid input:",err)  

if __name__ == "__main__":
    createset = CreateSet()
    createset.create_a_set() 