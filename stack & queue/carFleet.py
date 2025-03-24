def carFleet(target,position,speed):
    pair = [[p,s] for p,s in zip(position,speed)]
    stack = []
    for p, s in sorted(pair)[::-1]:
        stack.append((target-p)/s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


target = 10
position = [1,4]
speed = [3,2]
print(carFleet(target,position,speed))