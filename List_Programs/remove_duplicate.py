''' 
  @Author: Uthsavi KP
  @Date: 2021-01-05 16:12:57
  @Last Modified by:   Uthsavi KP
  @Last Modified time: 2021-01-05 18:39:15  
  @Title: To remove duplicates from a list .
'''

class Duplicate:
    def __init__(self):
        pass
    def duplicate_removal(self):
        """
        removing duplicates from a list
        """
        duplicate = []
        number = int(input("Enter the number: "))
        for _ in range(number):
            values = int(input("Enter the elements: "))
            if values not in duplicate:
                duplicate.append(values)
        print("Values after removing duplicate items:", duplicate)    

if __name__ == "__main__":
    dup = Duplicate()
    dup.duplicate_removal()       