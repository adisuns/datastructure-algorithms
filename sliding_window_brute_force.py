class slidingWindow:
    
    arr = []
    window_size =0
    max_sum = 0
    
    
    def getMaxSum(self,arr,k):
        n = len(arr)
        if n <= k:
            print("invalid operation")
            return -1
        window_sum = sum(arr[i] for i in range(k))
        print("first window sum is ",window_sum)
        max_sum = window_sum
        
        for i in range(n-k):
            window_sum = window_sum - arr[i] + arr[i+k]
            print("other window sum is ",window_sum)
            self.max_sum = max(window_sum,max_sum)
        
    
    def __init__(self,arr,window_size):
        self.arr = arr
        self.window_size = window_size
        self.getMaxSum(self.arr,self.window_size)
        
        
arr = [80,-50,70,100,200,180]
window_size = 2
s = slidingWindow(arr,window_size)
print("final max sum is ",s.max_sum)