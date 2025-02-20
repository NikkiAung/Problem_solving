# s1 -> s2 until s1 empty
# x -> s1
# s2 -> s1

# Solu 1
class QueueSolu1:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self,x: int) -> None:
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        print("The element pushed is", x)
        self.s1.append(x)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        if len(self.s1) == 0:
            print("Stack is empty")
            return
        return self.s1.pop()

    def Top(self) -> int:
        if len(self.s1) == 0:
            print("Stack is empty")
            return
        return self.s1[-1]

    def size(self) -> int:
        return len(self.s1)


# if top pop when s2 empty, s1 -> s2

# Solu 2
class QueueSolu2:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self,x: int) -> None:
        print("The element pushed is ", x)
        self.s1.append(x)

    def pop(self) -> int:
        if len(self.s2) == 0:
            while len(self.s1) != 0:
               self.s2.append(self.s1.pop())  
        return self.s2.pop()

    def Top(self) -> int:
        if len(self.s2) == 0:
            while len(self.s1) != 0:
               self.s2.append(self.s1.pop())  
        return self.s2[-1]

    def size(self) -> int:
        return len(self.s1)+len(self.s2)
    


if __name__ == "__main__":
    q = QueueSolu1()
    q.push(3)
    q.push(4)
    print("The element poped is", q.pop())
    q.push(5)
    print("The top of the queue is", q.Top())
    print("The size of the queue is", q.size())

    print('*' * 100)

    q = QueueSolu2()
    q.push(3)
    q.push(4)
    print("The element poped is", q.pop())
    q.push(5)
    print("The top of the queue is", q.Top())
    print("The size of the queue is", q.size())