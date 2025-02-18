class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_val = val
            self.stack.append(val)
        else:
            if val < self.min_val:
                self.stack.append(2*val-self.min_val)
                self.min_val = val
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        
        val = self.stack.pop()
        if val < self.min_val:
            self.min_val = 2*self.min_val-val

    def top(self) -> int:
        if not self.stack:
            return -1
        val = self.stack[-1]
        if val < self.min_val:
            return self.min_val
        return val

    def getMin(self) -> int:
        return self.min_val if self.stack else -1  # Handle empty stack case 
        
