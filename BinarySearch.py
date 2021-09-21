class binarySearch :
    
    sortedList = []
    taeget = 0
     
    def performSearch(self,sorted_list, target):
        left_pointer = 0
        right_pointer = len(sorted_list) - 1
        
        while left_pointer <= right_pointer:
            mid = (left_pointer + right_pointer) // 2
            if sorted_list[mid] == target:
                return mid
            elif sorted_list[mid] < target:
                left_pointer = mid + 1
            else:
                right_pointer = mid - 1
        
        return -1
     
    def __init__(self,listOfNumbers, target):
        self.target = target
        listOfNumbers.sort()
        pos  = self.performSearch(listOfNumbers,target)   
        print("target found at position of index ",pos)

"""
sanple run
"""

lists = [1,4,2,6,3,7,9,8]
target = 8
bs = binarySearch(lists,target) 
    
    