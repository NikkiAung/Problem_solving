def isPalindrome(s):
    l, r = 0, len(s)-1
    while l <= r:
        if not s[l].isalnum():
            l+=1
        elif not s[r].isalnum():
            r-=1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l+=1
            r-=1
    return True

s = "Was it a car or a cat I saw?"
print(isPalindrome(s))
