''' 
@Author: Uthsavi KP
@Date: 2021-01-05 13:09:23
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 13:25:05 
@Title : To Create Tuple  
'''

class CreateTuple:
  def __init__(self):
    pass
  def get_tuple(self):
    """
    creating a tuple
    """
    try:
      tuple_elements = tuple(input("Enter tuple elements: "))
      print(tuple_elements)
    except Exception as err:
      print("Invalid input:",err)  

if __name__ == "__main__":
  create = CreateTuple()
  create.get_tuple()