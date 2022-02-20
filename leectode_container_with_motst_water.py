from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        maxarea = 0
        print("left ",left)
        print(" right  ",right)
        print(" max area ",maxarea)

        while left < right:
            minheight = min(height[left],height[right])
            diff = right -left
            temparea = minheight * diff
            maxarea = max(maxarea, temparea)
        if height[left] < height[right]:
            left +=1
        else:
            right-=1
        
        if left == right:
            return maxarea

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
area = s.maxArea(height)
print(area)