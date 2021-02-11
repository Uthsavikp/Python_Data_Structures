''' 
@Author: Uthsavi KP
@Date: 2021-01-05 08:25:53
@Last Modified by:   Uthsavi KP
@Last Modified time: 2021-01-05 08:25:53 
@Title: To Find The Intersection Of Sets. 
'''

class Intersection:
    def intersection_set(self):
        """
        finding intersection of set
        """
    try:
        set_elements = set(input("Enter tuple elements: "))
        set_elements1 = set(input("Enter tuple elements: "))
        set1 = set_elements.intersection(set_elements1)
        print("Intersection of set")
        print(set1)
    except Exception as err:
        print("Invalid input:",err)  

if __name__ == "__main__":
    intersect = Intersection()
    intersect.intersection_set() 