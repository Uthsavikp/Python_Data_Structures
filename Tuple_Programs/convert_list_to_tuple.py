''' 
@Author: Uthsavi KP
@Date: 2021-01-05 08:25:53
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 08:25:53  
@Title : To Convert List To Tuple
'''

class ListToTuple:
    def __init__(self):
        self.list_items = [1,9,2,8,3]
    def list_to_tuple_conversion(self):
        """
        converting list to tuple
        """
        
        print(tuple(self.list_items))
       
if __name__ == "__main__":
    listtotuple = ListToTuple()
    listtotuple.list_to_tuple_conversion()