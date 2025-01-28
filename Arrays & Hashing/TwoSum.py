from collections import defaultdict
def TwoSum(nums,target):
    hash_map = defaultdict(int)
    for i in range(len(nums)):
        complement = target-nums[i]
        if complement in hash_map:
            return [hash_map[complement],i]
        hash_map[nums[i]] = i
    return []


nums = [1,2,3,4]
target = 5
print(TwoSum(nums,target))

#Time Complexity O(n)
#Space Complexity O(n)