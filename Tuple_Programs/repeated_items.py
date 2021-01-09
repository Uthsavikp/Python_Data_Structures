''' 
@Author: Uthsavi KP
@Date: 2021-01-05 08:25:53
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 08:49:04
@Title: To Remove Repeated Items From Tuple 
'''

class RepeatedItems:
    def __init__(self):
        pass
    def repeated_item_in_tuple(self):
        """
        finding repeated items of a tuple
        """
        try:
            tuple_elements = tuple(input("Enter tuple elements: "))
            repeat = []
            for element in tuple_elements:
                if tuple_elements.count(element)>1:
                    if element not in repeat:
                        repeat.append(element)
            print("Repeated items: ",tuple(repeat))
        except Exception as err:
            print("Invalid input: ",err)            

if __name__ == "__main__":
    repeated = RepeatedItems()
    repeated.repeated_item_in_tuple()