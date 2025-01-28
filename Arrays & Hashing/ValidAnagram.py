#Solu1
from collections import Counter
def ValidAnagram1(s,t):
    if Counter(s) == Counter(t):
        return True
    else:
        return False
#Time Complexity O(n)
#Space Complexity O(n)

#Solu2
from collections import defaultdict
def ValidAnagram2(s,t):
    if len(s) != len(t):
        return False
    
    count = [0]*26

    for i in range(len(s)):
        count[ord(s[i])-ord('a')] += 1
        count[ord(t[i])-ord('a')] -= 1
    
    for val in count:
        if val != 0:
            return False
    return True

s = "racecar"
t = "carrace"
print(ValidAnagram2(s,t))

#Time Complexity O(n)
#Space Complexity O(1)