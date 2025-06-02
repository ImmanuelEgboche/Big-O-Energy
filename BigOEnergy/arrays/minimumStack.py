class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack: # check if empty
            self.minStack.append(val)
        else:
            # if not empty
            self.minStack.append(min(val, self.minStack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        # getting the minimum element in O(1) time unless its ordered??
        if self.minStack:
            return self.minStack[-1]