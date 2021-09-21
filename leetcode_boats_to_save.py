#leetcode problem 881
class Solution:
    
    def numRescueBoats(self, people,limit):
        people.sort()
        left_pointer = 0
        right_pointer = len(people) -1
        number_boats = 0
        
        while(left_pointer <= right_pointer):
            if left_pointer == right_pointer:
                number_boats+=1
                break
                
            if people[left_pointer] + people[right_pointer] <=limit:
                left_pointer+=1
                
            right_pointer -=1
            number_boats+=1
            
        return  number_boats
    
people = [1,3,2]
limit = 3
s = Solution()
boats = s.numRescueBoats(people, limit)
print(boats)