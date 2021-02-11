''' 
  @Author: Uthsavi KP
  @Date: 2021-01-08 23:27:24
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-08 23:27:24
  @Title: To convert a list into a nested dictionary of keys
'''

class NestedDictionary:
  def get_nested_dictionary(self):
    """
    converting list to nested dictionary
    using list comprehension 
    """
    list1 = ["abc", 'to', 'xyz'] 
    list2 = ['good', 'better', 'best'] 
    list3 = [2, 4, 6] 
   
    nested_dictionary = [{a: {b: c}} for (a, b, c) in zip(list1, list2, list3)] 
  
    print("Nested dictionary :",nested_dictionary)

if __name__ == "__main__":
    nested_dict = NestedDictionary()
    nested_dict.get_nested_dictionary()    