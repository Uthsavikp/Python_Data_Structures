

'''
* @Author: Uthsavi KP
* @Date: 2020-01-06 23:12:49 
* @Last Modified by: Uthsavi KP
* @Last Modified time: 2020-01-06 23:12:49
* @Title: To find maximum and minimum numbers.
'''

class MaxMin:
    def find_max_min(self,data):
        """
        finding maximum and minimum numbers
        """
        maximum = data[0]
        minimum = data[0]
        for num in data:
            if num> maximum:
                maximum = num
            elif num< minimum:
                minimum = num
        return maximum, minimum

if __name__ == "__main__":
    maxmin = MaxMin()
    print(maxmin.find_max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))