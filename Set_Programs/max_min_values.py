''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 15:09:48
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-06 19:48:03
  @Title: To find maximum and the minimum value in a set.
'''

class MaxMin:
    def get_max_min_values(self):
        """
        getting minimum and maxium value in set
        """
        try:
            set_values = set(input("Enter your values :"))
            print("Maximum value in set :",min(set_values))
            print("Minimum value in set :",max(set_values))
        except Exception as err:
            print(err)
        
if __name__ == "__main__":
    max_min = MaxMin()
    max_min.get_max_min_values()        