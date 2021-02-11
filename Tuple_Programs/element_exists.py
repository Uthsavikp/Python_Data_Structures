''' 
@Author: Uthsavi KP
@Date: 2021-01-05 14:20:22
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 16:22:46
@Title: To Check If An Element Exists In In The Tuple. 
'''

class ElementExists:
    def __init__(self):
        pass
    def element_exists_in_tuple(self):
        """
        finding if a element exists within a tuple
        """
        try:
            tuple_elements = (1,2,"black","white",47,"35",{"A":4},(2,),[4,8],4,100)
            print(5 in tuple_elements)   #using membership operator
            print("black" in tuple_elements)
            print({"A":4} in tuple_elements)
            print("x" in tuple_elements)
            print("x" not in tuple_elements)
            print((2,) in tuple_elements)

        except Exception as err:
            print(err)            

if __name__ == "__main__":
    exists = ElementExists()
    exists.element_exists_in_tuple()