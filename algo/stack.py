class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            mi = min(self.min_stack[-1], val)
        else:
            mi = val
        self.min_stack.append(mi)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.min_stack:
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
