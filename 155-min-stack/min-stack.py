
"""
push 3, 2, 5
 0 1 2
[3,2,5]
min val     3 2 2
min val idx [0 1 1]

"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val_idx = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_val_idx) != 0:
            if val < self.stack[self.min_val_idx[-1]]:
                self.min_val_idx.append(len(self.stack)-1)
        else:
            self.min_val_idx.append(0)


    def pop(self) -> None:
        if len(self.min_val_idx) != 0:
            if len(self.stack)-1 == self.min_val_idx[-1]:
                self.min_val_idx.pop(-1)
        self.stack.pop(-1)

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.min_val_idx[-1]]
        

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()