from collections import Counter
def topKFrequent(nums, k):
    frequent_dict = Counter(nums)

    freq = [[] for i in range(len(nums)+1)]
    for n, c in frequent_dict.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
            
nums = [1,1,1,2,2,3]
k = 2

#Time Complexity O(n)
#Space Complexity O(n)