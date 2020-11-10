# %%


class StackOfPlates:
    def __init__(self, capacity=3):
        self.stacks = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.stacks) == 0

    def is_last_full_(self):
        return len(self.stacks[-1]) == self.capacity

    def is_last_emptish_(self):
        return len(self.stacks[-1]) == 1

    def push(self, value):
        if self.is_empty() or self.is_last_full_():
            self.stacks.append([value])
        else:
            self.stacks[-1].append(value)

    def peek(self):
        if self.is_empty():
            raise Exception("empty")
        value = self.stacks[-1][-1]
        return value

    def pop(self):
        if self.is_empty():
            raise Exception("empty")
        value = self.stacks[-1][-1]
        if self.is_last_emptish_():
            self.stacks.pop()
        else:
            self.stacks[-1].pop()
        return value


stack = StackOfPlates()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.peek()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.stacks
# %%


# %%
# %%
# %%
# %%

