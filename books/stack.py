
from collections import deque

class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        return self.stack.appendleft(x)

    def pop(self) -> int:
        print(self.stack.pop())

    def top(self) -> int:
        print(self.stack.popleft())

    def empty(self) -> bool:
        stack = self.stack = deque()
        return stack



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(3)
obj.push(5)
obj.push(6)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()