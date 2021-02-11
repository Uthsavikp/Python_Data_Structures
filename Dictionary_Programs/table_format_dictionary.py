''' 
  @Author: Uthsavi KP
  @Date: 2021-01-08 14:20:26
  @Last Modified by: Uthsavi KP
  @Last Modified time: 2021-01-08 14:20:26
  @Title: To print a dictionary in table format. 
'''

class TableFormat:
    def table_format(self):
        """
        printing dictionary in a table format
        """
  
        dict1 = {(0, 0): 'Berlin', (0, 1): 21, (0, 2): 'Male', 
                 (1, 0): 'Rachel', (1, 1): 20, (1, 2): 'Female', 
                 (2, 0): 'Samuel', (2, 1): 21, (2, 2): 'Male'
                } 
  
        # printing the name of the columns. 
        print(" NAME ", " AGE ", "  GENDER " ) 
        for i in range(3): 
            for j in range(3): 
                print(dict1[(i, j)], end ='   ') 
          
            print() 
if __name__ == "__main__":
    table = TableFormat()
    table.table_format()            