class Queue:
    def __init__(self):
        self.queue = list()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        item = self.queue[0]
        self.queue = self.queue[1:]
        return item

    def is_empty(self):
        return (len(self.queue) == 0)
