''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 23:27:24
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-06 23:57:31
  @Title: To find the union of sets.
'''

class SetUnion:
    def get_union_of_sets(self):
        """
        ceating the union of two sets
        """
        my_set1 = set(input("Enter set one elements: "))
        my_set2 = set(input("Enter set two elements: "))

        union_of_both_sets = my_set1.union(my_set2)
        print("Union of two sets is :", union_of_both_sets)

if __name__ == "__main__":
    set_union = SetUnion()
    set_union.get_union_of_sets()        