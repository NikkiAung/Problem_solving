#Solu 1
# from collections import Counter
# def checkInclusion(s1, s2):
#     n = len(s1)
#     for i in range(len(s2)-(n-1)):
#         if Counter(s1) == Counter(s2[i:i+n]):
#             return True
#     return False

def checkInclusion(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    if s1_len > s2_len:
        return False
    
    l,r = 0,0
    s1_hash = [0]*26
    s2_hash = [0]*26
    while r < s1_len:
        s1_hash[ord(s1[r])-ord('a')] +=1
        s2_hash[ord(s2[r])-ord('a')] +=1
        r+=1
    r-=1
    while r < s2_len:
        if s1_hash == s2_hash:
            return True
        r+=1
        if r != s2_len:
            s2_hash[ord(s2[r])-ord('a')] +=1
        s2_hash[ord(s2[l])-ord('a')] -=1
        l+=1
    return False

s1 = "abc"
s2 = "lecabee"

print(checkInclusion(s1,s2))