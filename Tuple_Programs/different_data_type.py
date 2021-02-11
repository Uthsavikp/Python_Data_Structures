''' 
@Author: Uthsavi KP
@Date: 2021-01-05 13:42:48
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 14:53:18
@Title: To Create Different A Tuple With Different Data Types  
'''

class DifferentTuple:
  def __init__(self):
    pass
  def tuple_with_different_data_type(self):
    """
    creating a tuple with different data type
    """
    tuple_elements = (1,2,"string",2.3,True)
    print(tuple_elements)

if __name__ == "__main__":
  create = DifferentTuple()
  create.tuple_with_different_data_type()