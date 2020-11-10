# %%


class Node:
    def __init__(self, value, next):
        self.Value = value
        self.Next = next


class Stack:
    def __init__(self):
        self.Head = None

    def is_empty(self):
        return self.Head == None

    def push(self, value):
        self.Head = Node(value, self.Head)

    def pop(self):
        if self.is_empty():
            raise Exception("Empty")
        else:
            res = self.Head.Value
            self.Head = self.Head.Next
            return res

    def peek(self):
        if self.is_empty():
            raise Exception("Empty")
        else:
            res = self.Head.Value
            return res


class MinStack:
    def __init__(self):
        self.ValueStack = Stack()
        self.Min = Stack()

    def is_empty(self):
        return self.ValueStack.is_empty()

    def peek(self):
        return self.ValueStack.peek()

    def pop(self):
        value = self.ValueStack.pop()
        minval = self.Min.peek()
        if minval == value:
            self.Min.pop()
        return value

    def min(self):
        return self.Min.peek()

    def push(self, value):
        if self.is_empty():
            self.ValueStack.push(value)
            self.Min.push(value)
        else:
            minval = self.Min.peek()
            if value <= minval:
                self.Min.push(value)
            self.ValueStack.push(value)


# %%
minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(3)
minStack.push(-1)
minStack.pop()
minStack.pop()
minStack.pop()
minStack.pop()
minStack.min()

# minStack.pop()


# %%
