def ValidParentheses(s):
    bracket_dict = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    stack = []
    for c in s:
        if c in bracket_dict:
            if stack and stack[-1] == bracket_dict[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

s = "([{}])"
print(ValidParentheses(s))