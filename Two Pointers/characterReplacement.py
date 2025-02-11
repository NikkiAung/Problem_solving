from collections import defaultdict
def characterReplacement(s,k):
    l,r = 0,0
    hash_map = defaultdict(int)
    res = 0
    while r < len(s):
        hash_map[s[r]]+=1
        if hash_map:
            maxFreq = max(hash_map.values())
        changes = (r-l+1) - maxFreq
        while changes > k:
            hash_map[s[l]]-=1
            l+=1
            maxFreq = max(hash_map.values())
            changes = (r-l+1) - maxFreq
        res = max(res,r-l+1)
        r+=1
    return res

s = "XYYX"
k = 2
print(characterReplacement(s,k))