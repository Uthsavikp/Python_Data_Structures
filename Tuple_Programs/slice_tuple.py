''' 
@Author: Uthsavi KP
@Date: 2021-01-05 20:12:19
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 22:38:33
@Title: To Slice A Tuple    
'''

class SliceTuple:
    def slice_a_tuple(self):
        """
        slice a tuple
        """
        tuple_elements = (3,43,65,21,89,0)
        print(tuple_elements[::-1])
        print(tuple_elements[2:5])
        print(tuple_elements[:])
        print(tuple_elements[-1:-4:-1])
        print(tuple_elements[-3:-5:-1])
        print(tuple_elements[2])

if __name__ == "__main__":
    slicetuple = SliceTuple()
    slicetuple.slice_a_tuple()