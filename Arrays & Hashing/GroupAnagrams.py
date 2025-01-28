from collections import defaultdict
def GroupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0]*26
        for chr in s:
            count[ord(chr)-ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(GroupAnagrams(strs))

#Time Complexity O(n*m)
#Space Complexity O(n)