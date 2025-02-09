def Two_Integer_Sum_II(numbers,target):
    i = 0
    while i < len(numbers):
        j = i+1
        while j < len(numbers):
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            j+=1
        i+=1


numbers = [1,2,3,4] 
target = 3
print(Two_Integer_Sum_II(numbers,target))