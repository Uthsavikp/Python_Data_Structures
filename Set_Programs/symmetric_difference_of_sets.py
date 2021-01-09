''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 23:27:24
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-06 23:57:31
  @Title: To find the symmetric difference between two sets.
'''

class SymmeticDifference:
    def get_symmetric_difference(self):
        """
        getting the symmetic difference of two sets,
        it gets the elements which are only in my_set1 
        and elements which are only in my_set2
        """
        try:
            my_set1 = set(input("Enter set one elements :"))
            my_set2 = set(input("Enter set two elements :"))

            symmetric_difference_set = my_set1.symmetric_difference(my_set2)
            print("Symmetric difference of two set is :",symmetric_difference_set)
        except Exception as err:
            print(err)

if __name__ == "__main__":
    symmetric_diff = SymmeticDifference()
    symmetric_diff.get_symmetric_difference()        