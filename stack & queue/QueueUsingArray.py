class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.currSize = 0
        self.maxSize = 16
        self.arr = [0]*self.maxSize 

    def push(self, num: int) -> None:
        if self.currSize == self.maxSize:
            print('Queue is full!')
            return

        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            self.end = (self.end+1)%self.maxSize
        self.arr[self.end] = num
        self.currSize += 1

    def pop(self) -> int:
        if  self.start == -1:
            print('Queue is empty!')
            return
        pop = self.arr[self.start]

        if self.currSize == 1:
            self.start = -1
            self.end = -1
        else:
            self.start = (self.start+1)%self.maxSize

        self.currSize -= 1
        return pop

    def top(self) -> int:
        if self.start == -1:
            print('Queue is empty!')
            return
        return self.arr[self.start]
    
    def size(self) -> int:
        return self.currSize

        

if __name__ == "__main__":
    q = Queue()
    q.push(4)
    q.push(14)
    q.push(24)
    q.push(34)
    print("The peek of the queue before deleting any element", q.top())
    print("The size of the queue before deletion", q.size())
    print("The first element to be deleted", q.pop())
    print("The peek of the queue after deleting an element", q.top())
    print("The size of the queue after deleting an element", q.size())