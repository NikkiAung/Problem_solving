def productExceptSelf(nums):
        l_mul = 1
        r_mul = 1
        l_arr = [0] * len(nums)
        r_arr = [0] * len(nums)
        for i in range(len(nums)):
            j = -i-1
            l_arr[i] = l_mul
            r_arr[j] = r_mul
            l_mul *= nums[i]
            r_mul *= nums[j]
        print(l_arr)
        print(r_arr)

nums = [1,2,3,4]
productExceptSelf(nums)