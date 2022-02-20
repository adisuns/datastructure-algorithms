palindrome = lambda mystr :  mystr if mystr == mystr[::-1] else -1
def Solution(str_list,size):
    
    if size ==0:
        return [[]]
    temp = []
    for i in range(0,len(str_list)):
        num1 = str_list[i]
        list1 = str_list[i+1:]
        for num2 in Solution(list1,size-1):
            number = num1+''.join(num2)
            temp.append(number)
                       
    return temp
  


i = 1
mystr = "009009"
palindromeList = []
while i <= len(mystr):
    templist = Solution([x for x in mystr], i)
    for t in templist:
        if palindrome(t) != -1:
            if t not in palindromeList:
                palindromeList.append(int(t))
    i+=1

print(palindromeList)
print(max(palindromeList))