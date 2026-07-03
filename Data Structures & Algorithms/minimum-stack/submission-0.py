class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = val
        if self.stack and self.stack[-1][1] < val:
            min_val = self.stack[-1][1]
        self.stack.append((val, min_val))


    def pop(self) -> None:
        if not self.stack:
            return False
        curr_val = self.stack[-1][0]
        self.stack.pop()
        return curr_val

    def top(self) -> int:
        if not self.stack:
            return False
        top_val = self.stack[-1][0]
        return top_val

    def getMin(self) -> int:
        if not self.stack:
            return False
        min_val = self.stack[-1][1]
        return min_val
