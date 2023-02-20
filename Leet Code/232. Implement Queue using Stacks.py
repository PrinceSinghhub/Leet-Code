class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        stack2 = []
        # Everytime we push an element into stack, with the help of stack2
        # I am reversing the stack so that top element in the stack will be
        # the first-in element
        while self.stack1:
            stack2.append(self.stack1.pop())

        self.stack1.append(x)

        while stack2:
            self.stack1.append(stack2.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack1.pop()

    def peek(self):
        """
        Get the front element.
        """
        return self.stack1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0

ans = MyQueue()
