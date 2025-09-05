class Stack:
    def __init__(self, size=5):
        self.stack = []
        self.size = size

    def push(self, item):
        if len(self.stack) >= self.size:
            self.stack.pop(0)  # remove oldest
        self.stack.append(item)

    def view(self):
        print("Recently Viewed:")
        for item in reversed(self.stack):
            print(item)
