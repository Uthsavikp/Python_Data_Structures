''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 17:34:52
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-06 17:34:52
  @Title: To concatenate dictionaries to create a new one.
'''

class Concatenate:
    def __init(self):
        """
        defining dictionaries
        """
        self.dic1
        self.dic2
        self.dic3

    def new_dictionary(self):
        """
        concatenate new dictionary to get a new one
        """
        self.dic1={1:10, 2:20}
        self.dic2={3:30, 4:40}
        self.dic3={5:50, 6:60}
        dic4={**self.dic1 , **self.dic2 , **self.dic3}  
        print("new dictionary :", dic4)    	

if __name__ == "__main__":
    concat = Concatenate()
    concat.new_dictionary()