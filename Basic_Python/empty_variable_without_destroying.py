'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 02:27:36 
* @Last Modified by: Uthsavi KP
* @Last Modified time: 2020-01-05 02:27:36
* @Title : To empty variable without destroying it..
'''

class EmptyVariable:
    def empty_variable(self):
        """
        emptying variable without destroying them
        """
        n = 20
        d = {"x":200}
        print(type(n)())
        print(type(d)())
         
if __name__ == "__main__":
    emp_variable = EmptyVariable()
    emp_variable.empty_variable()      