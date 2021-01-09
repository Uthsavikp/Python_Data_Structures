''' 
  @Author: Uthsavi KP
  @Date: 2021-01-06 23:27:24
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-06 23:57:31
  @Title: To find the list of words that are longer than n from a given list of words.
'''

class LongestLength:
    def __init__(self):
        pass
    def get_length_of_longest(self):
        """
        getting the length of the longest word
        """
        try:
            list_of_words = input("Enter list of words separated by comma: ")
            longest_length = []
            for value in list_of_words.split(","):
                word_length = int(input("Enter word length :"))
                if len(value) > word_length:
                        longest_length.append(value)
                print("Longest words are ",longest_length)
        except Exception as err:
            print(err)        
      
if __name__ == "__main__":  
    lng = LongestLength()
    lng.get_length_of_longest()
