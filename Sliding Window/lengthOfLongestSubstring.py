def lengthOfLongestSubstring(s):
    l,r = 0,0
    res = 0
    dict = {}
    while r < len(s):
        if s[r] in dict and l <= dict[s[r]]:
            l = dict[s[r]] + 1
        dict[s[r]] = r
        res = max(res,r-l+1)
        r+=1
    return res

s = "abcabcbb"
print(lengthOfLongestSubstring(s))