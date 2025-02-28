## Brute force solu1
def evalRPN(tokens):
    while len(tokens) > 1:
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                a = int(tokens[i-2])
                b = int(tokens[i-1])
                if tokens[i] == '+':
                    result = a + b
                elif tokens[i] == '-':
                    result = a - b
                elif tokens[i] == '*':
                    result = a * b
                elif tokens[i] == '/':
                    result = int(a / b)
                tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
                break
    return int(tokens[0])

tokens = ["1","2","+","3","*","4","-"]
print(evalRPN(tokens))


# Stack solu2
def evalRPN(tokens):
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop()+stack.pop())
        elif c == "-":
            a, b = stack.pop(),stack.pop()
            stack.append(b-a)
        elif c == "*":
            stack.append(stack.pop()*stack.pop())
        elif c == "/":
            a, b = stack.pop(),stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(c))
    return stack[0]
