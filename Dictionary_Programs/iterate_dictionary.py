''' 
  @Author: Uthsavi KP
  @Date: 2021-01-07 20:33:39
  @Last Modified by: Uthsavi KP
  @Last Modified time: 2021-01-07 20:33:39
  @Title: To iterate over dictionaries using for loops. 
'''

class IterateDictionary:
    def __init(self):
        self.dictionary_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        
    def iterate_over_dictionary(self):
        """
        iterating over dictionary using for loops
        """
        for key, value in self.dictionary_data.items():
            print(key, value)

if __name__ == "__main__":
    iteratedict = IterateDictionary()
    iteratedict.iterate_over_dictionary()