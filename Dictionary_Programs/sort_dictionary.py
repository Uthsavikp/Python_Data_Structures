''' 
  @Author: Uthsavi KP
  @Date: 2021-01-07 15:08:14
  @Last Modified by: Uthsavi KP
  @Last Modified time: 2021-01-07 15:08:14
  @Title: To sort items in dictionary.
'''

class SortItems:
    def __init(self):
        pass
    def sort_ascending_descending(self):
        """
        sorting in ascending and descending order
        """ 
        dictionary_data = {'a': 1, 'c': 2, 'd': 3, 'x': 4, 'e': 5}

        print(sorted(dictionary_data.items(), key=lambda element: element[1]))
        print(sorted(dictionary_data.items(), key=lambda element: element[1], reverse=True))


if __name__ == "__main__":
    sort_items = SortItems()
    sort_items.sort_ascending_descending()        