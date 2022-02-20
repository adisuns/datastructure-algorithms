from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        pointer = 1
        while pointer < len(arr) and arr[pointer] > arr[pointer -1]:
            pointer +=1
        if pointer == 1 or pointer == len(arr):
            return False
        while pointer < len(arr) and arr[pointer] < arr[pointer -1]:
            pointer +=1
            
        return  pointer == len(arr)

s = Solution()
arr = [0,3,2,1]
flag = s.validMountainArray(arr)
print(flag)         