''' 
  @Author: Uthsavi KP
  @Date: 2021-01-09 02:43:36
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-01-09 02:43:36
  @Title: To check multiple keys exists in a dictionary.
'''

class CheckKeys:
    def multiple_keys(self):
      """
      checking multiple keys exists in a dictionary
      using comparison operator
      """
      person = {"good" : 1, "bad" : 2, "excellent" :3} 
      print(person.keys() >= {"good", "bad"}) 
      print(person.keys() >= {"excellent", "calm"})

if __name__ == "__main__":
    check_keys = CheckKeys()
    check_keys.multiple_keys()