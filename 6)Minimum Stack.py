class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push to min_stack if it's empty or val is smaller/equal to current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
'''stack: for normal values

min_stack: only stores the minimums, ensuring getMin() is always O(1)

Every time we push, we also push to min_stack only if the pushed value is ≤ current min.

When we pop, if the popped value is equal to the current min, we also pop it from min_stack.'''