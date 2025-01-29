def longestConsecutive(nums):
    setNum = set(nums)
    maxCount = 0
    for num in setNum:
        if num-1 not in setNum:
            count = 1
            currNum = num
            while currNum+1 in setNum:
                count+=1
                currNum+=1
            maxCount = max(maxCount,count)
    return maxCount
    
nums = [2,20,4,10,3,4,5]
print(longestConsecutive(nums))

#Time Complexity O(n)
#Space Complexity O(n)