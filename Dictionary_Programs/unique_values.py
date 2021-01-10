''' 
  @Author: Uthsavi KP
  @Date: 2021-01-07 14:18:13
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-07 14:18:13
  @Title: To print all unique values in a dictionary.
'''

class UniqueValues:
    def __init(self):
        pass
    def get_unique_values(self):
        """
        to get all unique values in a dictionary
        """
        dictionary_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
        
        print("Original dictionary :", dictionary_data)
        print("Unique values :", list(set(val for items in dictionary_data for val in items.values())))

if __name__ == "__main__":
    uniq_values = UniqueValues()
    uniq_values.get_unique_values()