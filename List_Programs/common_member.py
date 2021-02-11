''' 
  @Author: Uthsavi KP
  @Date: 2021-01-05 21:19:44
  @Last Modified by:   Uthsavi KP
  @Last Modified time: 2021-01-05 21:19:44  
  @Title: Return True If The Lists Have Common Member.
'''

class TwoList:
    def __init__(self):
        pass
    def common_in_two_list(self,list_one,list_two):
        """
        Returns True if list one and list two have any common elements 
        """         
        result = False
        for val1 in list_one:
            for val2 in list_two:
                if val1 == val2:
                    result = True
                    return result
        return result
if __name__ == "__main__":
    two = TwoList()
    print(two.common_in_two_list([21,42,64,"cow"],[52,42,"cow","64"]))