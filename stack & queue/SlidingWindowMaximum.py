from collections import deque  # Correct import

def SlidingWindowMaximum(nums,k):
    dq = deque()
    res = []
    for i in range(len(nums)):
        if (dq and dq[0] == i-k):
            dq.popleft()
        
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)

        if i >= k-1:
            res.append(nums[dq[0]])
    return res
        
nums = [1,2,1,0,4,2,6]
k = 3
print(SlidingWindowMaximum(nums,k))