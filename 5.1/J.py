class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack[-1]
        self.stack = self.stack[:-1]
        return item

    def is_empty(self):
        return (len(self.stack) == 0)
