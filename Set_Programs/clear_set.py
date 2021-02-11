''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 23:27:24
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-06 23:51:31
  @Title: To program to clear a set.
'''

class ClearSet:
    def to_clear_set(self):
        """
        to clear the set
        """
        try:
            my_set = set(input("Enter your set elements :"))
            my_set.clear()
            print("Set after clear :",my_set)
        except Exception as err:
          print(err)

if __name__ == "__main__":
    clr_set = ClearSet()
    clr_set.to_clear_set()        