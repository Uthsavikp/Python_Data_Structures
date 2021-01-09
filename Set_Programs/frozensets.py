''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 23:27:24
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-06 23:57:31
  @Title: To use frozensets
'''
class UseFrozensets:
    def get_frozensets(self):
      """
      to use frozensets
      """
      try:
          set_elements = frozenset(input("Enter tuple elements: "))
          print(set_elements)
      except Exception as err:
          print("Invalid input:",err)  

if __name__ == "__main__":
    use_frozensets = UseFrozensets()
    use_frozensets.get_frozensets()

    