'''
* @Author: Uthsavi KP
* @Date: 2020-01-06 18:16:02 
* @Last Modified by: Uthsavi KP
* @Last Modified time: 2020-01-06 18:16:0
* @Title : To extract single key-value pair of a dictionary in variables.
'''

class KeyValuePair:
    def extract_single_key_value_pair(self):
        """
        extracting single key value pair 
        """
        my_dict = {'Red': 'Green'}
        (dict_key, dict_value), = my_dict.items()
        print(dict_key)
        print(dict_value)

if __name__ == "__main__":
    key_value_pair = KeyValuePair()       
    key_value_pair.extract_single_key_value_pair()