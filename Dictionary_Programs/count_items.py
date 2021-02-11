''' 
  @Author: Uthsavi KP
  @Date: 2021-01-07 13:32:43
  @Last Modified by: Uthsavi KP
  @Last Modified time: 2021-01-07 13:32:43
  @Title: To count number of items in a dictionary value that is a list.
'''

class CountItems:
    def count_dictionary_values(self):
        """
        counting number of items in a dictionary value that is a list
        """
        my_dictionary = { 'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9], 
              'B' : 34, 
              'C' : 12, 
              'D' : [7, 8, 9, 6, 4] } 
  
        count = 0
        for key, value in my_dictionary.items(): 
            if isinstance(value, list): 
                count += len(value) 
        print("Number of items in a dictionary value i.e a list :",count) 
      
if __name__ == '__main__': 
    count_itm = CountItems()
    count_itm.count_dictionary_values() 