def threeSum(nums):
    sorted_num = sorted(nums)
    res = []
    for i in range(len(sorted_num)):
        if i != 0 and sorted_num[i] == sorted_num[i-1]:
            continue
        j = i+1
        k = len(sorted_num)-1
        while j < k:
            total_sum = sorted_num[i]+sorted_num[j]+sorted_num[k]
            if total_sum < 0:
                j+=1
            elif total_sum > 0:
                k-=1
            else:
                res.append([sorted_num[i], sorted_num[j], sorted_num[k]])
                j+=1
                k-=1
                while j < k and sorted_num[j] == sorted_num[j-1]:
                    j+=1
                while j < k and sorted_num[k] == sorted_num[k+1]:
                    k-=1
    return res

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))