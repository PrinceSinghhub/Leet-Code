class MinStack:

    def __init__(self):
        self.stack = []
        """
        initialize your data structure here.
        """

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def getMin(self):
        if not self.isEmpty():
            return min(self.stack)
        else:
            return -1