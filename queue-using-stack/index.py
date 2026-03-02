#implement queue using stack
#using 2 stack
#When push we will append to dynamic array, this will be a O(1) complexity
#when pop we will remove from s2, if s2 is empty, then enter the s1 into s2 inreverse way,
# then remove the last, pop will be a O(n)
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x: int) -> None:
        self.s1.append(x)
    
    def pop(self)-> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
    
    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
    
    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

# print(param_2)