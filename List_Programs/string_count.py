''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 21:23:49
  @Last Modified by:   Uthsavi KP
  @Last Modified time: 2021-01-05 22:58:01  
  @Title: To Count The Strings Inside List.
'''

class StringCount:
    def __init__(self):
        pass
    def count(self):
        """
        checking if the string length is 2 or more than 2
        checking if first and last character are same
        counting and printing the elements which satisfy these conditions
        """
        string_count = 0
        string = ['abc', 'xyz', 'aba', '1221']
        for elements in string:
            length = len(elements) 
            if length >= 2:
                if elements[0] == elements[-1]: 
                    string_count +=1
        print("String count :", string_count)
                    
if __name__ == "__main__":
    stringcount = StringCount()
    stringcount.count()