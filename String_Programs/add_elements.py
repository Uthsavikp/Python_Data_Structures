''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 23:27:24
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-06 23:57:31
  @Title: To add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
'''

class AddSufixes:
    
    def add_elements_at_end(self):
        """
        add sufixes ing or ly at end
        """
        try:
            user_input = input("Enter a number: ")
            if len(user_input) >=3:
                if user_input[-3:] != "ing":
                    user_input += "ing"
                else:
                    user_input += "ly"
            print(user_input)  
        except Exception as err:
            print(err)    
if __name__ == "__main__":
    add = AddSufixes()
    add.add_elements_at_end()