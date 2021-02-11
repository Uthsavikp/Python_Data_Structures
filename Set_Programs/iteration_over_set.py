''' 
@Author: Uthsavi KP
@Date: 2021-01-05 12:23:04
@Last Modified by: Uthsavi KP
@Last Modified time: 2021-01-05 14:46:19 
@Title: To Iterate Over A Set. 
'''

class Iteration:
    def __init__(self):
        pass
    def iterate_set(self):
        """
        iterating over a set
        """
    try:
        set_elements = set(input("Enter tuple elements: "))
        for num in set_elements:
            print(num)
    except Exception as err:
        print("Invalid input:",err)  

if __name__ == "__main__":
    iteration = Iteration()
    iteration.iterate_set() 