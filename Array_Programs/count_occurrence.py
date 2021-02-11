''' 
  @Author: Uthsavi KP
  @Date: 2021-01-08 19:17:12
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-08 19:32:52
  @Title: To get the number of occurrences of a specified element in an array
'''

class CountOccurance:
    def get_no_of_occurances(self):
        """
        counting the number of ocuurrences 
        """
        my_array = []

        try:
            for _ in range(int(input("Enter the number : "))):
                my_array.append(int(input("Enter the array elements : "))) 
            print("Array elements :",my_array)
            number_count = my_array.count(int(input("Enter the number you want to count :"))) 
            print("Number of occurance is :",number_count)    
        except Exception as err:
            print(err)

if __name__ == "__main__":
    count_occurance = CountOccurance()
    count_occurance.get_no_of_occurances()