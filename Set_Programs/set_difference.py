''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 23:27:24
  @Last Modified by: Uthsavi KP
  @Last Modified time: 2021-01-06 01:57:31
  @Title: To find the difference between two sets.
'''

class SetDifference:
    def get_set_difference(self):
        """
        getting set difference of my_set1 and my_set2
        and it outputs elements that are only in my_set1 
        but not in my_set2 and vice versa
        """
        try:
            my_set1 = set(input("Enter set one elements :"))
            my_set2 = set(input("Enter set two elements :"))

            only_my_set1_elements = my_set1.difference(my_set2)
            only_my_set2_elements = my_set2.difference(my_set1)

            print("Elements present only in my_set1 :",only_my_set1_elements)
            print("Elements present only in my_set2 :",only_my_set2_elements)
            print("Common elements from both sets :",str(only_my_set1_elements)+str(only_my_set2_elements))
        except Exception as err:
            print(err)
if __name__ == "__main__":
    set_diff = SetDifference()
    set_diff.get_set_difference()        