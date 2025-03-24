def DailyTemperatures(temperatures):
    res = [0]*len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and stack[-1][0] < t:
            stackT, stackInd =  stack.pop()
            res[stackInd] = i-stackInd
        stack.append([t,i])
    return res

temperatures = [73,74,75,71,69,72,76,73]
print(DailyTemperatures(temperatures))