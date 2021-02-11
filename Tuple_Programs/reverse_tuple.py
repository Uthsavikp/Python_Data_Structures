''' 
@Author: Uthsavi KP
@Date: 2021-01-05 17:37:13
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 19:46:21
@Title: To Reverse The Tuple Elements.  
'''

class ReverseTuple:
    def reverse_a_tuple(self):
        """
        reverse a tuple
        """
        tuple_elements = (3,43,65,"python","xyz",21,[2,3],89,0)
        print(tuple_elements[::-1])
        tuple1 = ("python_program")
        rev_tuple = reversed(tuple1)
        print(tuple(rev_tuple))
        
if __name__ == "__main__":
    reversetuple = ReverseTuple()
    reversetuple.reverse_a_tuple()