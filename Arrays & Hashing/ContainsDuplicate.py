def containDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

nums = [11,11,12,45,67,0]
print(containDuplicate(nums))

#Time Complexity O(n)
#Space Complexity O(n)