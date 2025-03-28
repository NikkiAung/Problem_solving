def largestRectangleArea(heights):
    stack = []
    maxArea = 0
    for i, h in enumerate(heights):
        start=i
        while stack and stack[-1][1] > h:
            stackInd, stackH = stack.pop()
            maxArea = max(maxArea,stackH*(i-stackInd))
            start=stackInd
        stack.append((start,h))
    for i, h in stack:
        maxArea = max(maxArea,h*(len(heights)-i))
    return maxArea

heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))