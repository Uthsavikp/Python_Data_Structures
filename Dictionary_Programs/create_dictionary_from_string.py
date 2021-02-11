''' 
  @Author: Uthsavi KP
  @Date: 2021-01-07 11:29:56
  @Last Modified by: Uthsavi KP
  @Last Modified time: 2021-01-07 11:29:56
  @Title: To create dictionary from string
'''

class CreateDictionary:
    def get_string_to_create_dictionary(self):
        """
        creating a dictionary from a string using dictionary comprehension
        """
        string_input = input("Enter your string : ")

        new_dictionary = {character: string_input.count(character) for character in string_input}

        print("New dictionary :",new_dictionary)

if __name__ == "__main__":
    create_dictionary = CreateDictionary()
    create_dictionary.get_string_to_create_dictionary()       