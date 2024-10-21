class Stack:
    def __init__(self):
        self.internalList = []

    def push(self, item):

        self.internalList.append(item)
    def pop(self):

        if len(self.internalList) == 0:
            return "Error: Stack is empty!"
        else:
            return self.internalList.pop()

    def peek(self):

        if not self.internalList:
            return "Error: Stack is empty!"
        return self.internalList[-1]
    def __str__(self):

        return self.internalList.__str__()