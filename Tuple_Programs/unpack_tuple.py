''' 
@Author: Uthsavi KP
@Date: 2021-01-05 19:02:16
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 22:43:27
@Title: To Unpack The Tuple Elements  
'''

class UnpackTuple:
  def __init__(self):
    pass
  def with_several_variables(self):
    """
    unpacking a tuple in several variables
    """
    tuple_elements = (24,96,"This","Is","Tuple",99)
    element1, element2, *element3, element4 = tuple_elements #using *args for tuple unpacking
    print(element1)
    print(element2)
    print(element3)
    print(element4)

if __name__ == "__main__":
  unpack = UnpackTuple()
  unpack.with_several_variables()