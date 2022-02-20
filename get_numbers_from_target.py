"""
given any lists of numbers, input is the target summ,
get 2 numbers whose addition is the target sum
"""

class Solution:
    def getNumbers(self,arr,target):
        for i in arr:
            num = target -i
            if num in arr:
                return num,i
            continue
       
                    
            
s = Solution()
arr = [1,3,2,1]
print(s.getNumbers(arr,3))