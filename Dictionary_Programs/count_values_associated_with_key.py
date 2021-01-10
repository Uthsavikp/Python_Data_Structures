''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 22:01:22
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-06 22:01:22
  @Title: To count how many dictionaries have success as True
'''

class ValueCount:
    def get_value_count(self):
        """
        counting the values associated with key in a dictionary
        """ 
        list_items =  [{'id': 1, 'success': True, 'name': 'Lary'}, 
                       {'id': 2, 'success': False, 'name': 'Rabi'}, 
                       {'id': 3, 'success': True, 'name': 'Alex'}]

        success_count = 0
        for dictionary_items in list_items:
            if 'success' in dictionary_items:
                if dictionary_items['success'] == True:
                    success_count +=1
        print("Success count as true is :",success_count)   

if __name__ == "__main__":
    value_count = ValueCount()
    value_count.get_value_count()                 