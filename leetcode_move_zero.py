#leetcode problem number 283
class Solution:
    
    
    def moveZeroes(self,arr):
       i = 0
       for num in arr:
           if num !=0 :
               arr[i] = num
               i+=1
    
       for j  in range(i,len(arr)):
           arr[j]=0
        
       return arr
        
           

arr = [0,1,0,3,0,0,12] 
print(arr)       
ret = Solution().moveZeroes(arr)
print(arr)