# %%
import numpy as np


class TriStack:

    def __init__(self, size_per_stack=10):
        self.size_per_stack = size_per_stack
        self.array = np.full(size_per_stack * 3, None)
        self.tails = [i * size_per_stack for i in range(3)]
        self.tails = np.array(self.tails)
        self.limits = [((i + 1) * size_per_stack) - 1 for i in range(3)]

    def is_empty(self, stack):
        return self.tails[stack] == self.size_per_stack * stack

    def pop(self, stack):
        if self.is_empty(stack):
            raise Exception(f"Stack {stack} is empty")
        else:
            value = self.array[self.tails[stack]]
            self.tails[stack] -= 1
            return value

    def peek(self, stack):
        if self.is_empty(stack):
            raise Exception(f"Stack {stack} is empty")
        else:
            value = self.array[self.tails[stack]]
            return value

    def can_add(self, stack):
        return self.tails[stack] <= self.limits[stack]

    def push(self, stack, value):
        if not self.can_add(stack):
            raise Exception(f"Stack {stack} is full")
        self.tails[stack] += 1
        self.array[self.tails[stack]] = value


# %%
tri = TriStack(3)
tri.tails
tri.is_empty(2)
tri.push(1,"A")
tri.push(1,"B")
tri.push(1,"C")
(tri.array, tri.tails)
tri.pop(1)
tri.pop(1)
tri.pop(1)
(tri.array, tri.tails)
# %% 
# %% 
# %% 
 v
