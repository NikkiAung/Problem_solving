def minWindow(s, t):
    m, n = len(s), len(t)
    if m < n:
        return ""

    hashArr = [0]*128
    for char in t:
        hashArr[ord(char)] += 1
    
    l, r = 0, 0
    count = 0
    minLen = float('inf')
    sIndex = -1

    while r < m:
        rightChar = s[r]
        if hashArr[ord(rightChar)] > 0:
            count += 1
        hashArr[ord(rightChar)] -= 1

        while count == n:
            if r-l+1 < minLen:
                minLen = r-l+1
                sIndex = l
            
            leftChar = s[l]
            hashArr[ord(leftChar)] += 1
            if hashArr[ord(leftChar)] > 0:
                count -= 1
            l+=1
        r+=1
    return "" if sIndex == -1 else s[sIndex:sIndex+minLen] 

s = "OUZODYXAZV"
t = "XYZ"

print(minWindow(s, t))
