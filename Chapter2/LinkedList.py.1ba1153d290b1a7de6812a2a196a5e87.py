# %%

from collections import defaultdict
import numpy as np


class Node:
    def __init__(self, value, next=None):
        self.Value = value
        self.Next = next


class LinkedList:
    def __init__(self):
        self.Head = None

    def is_empty(self):
        return self.Head == None

    def InsertBeginning(self, value):
        node = Node(value, self.Head)
        self.Head = node

    ## 2.1
    def remove_dups(self):
        if self.is_empty():
            return
        present = defaultdict(lambda: 0)
        current = self.Head
        present[current.Value] = 1
        while current != None:
            if current.Next != None and present[current.Next.Value] == 0:
                present[current.Next.Value] = 1
            elif current.Next != None and present[current.Next.Value] > 0:
                current.Next = current.Next.Next
                continue
            current = current.Next

    # 2.2
    def ith_element_aux(self, node, i):
        if node == None:
            return (False, -1, None)
        (res, ith, val) = self.ith_element_aux(node.Next, i)
        if res:
            return (res, ith, val)
        else:
            return (ith + 1 == i, ith + 1, node.Value)

    def ith_element(self, i):
        (res, ith, val) = self.ith_element_aux(self.Head, i)
        return (res, val)

    # 2.2 non recursive
    def ith_element_fast_slow(self, i):
        if self.is_empty():
            return False

        fast = self.Head
        slow = self.Head
        while fast.Next != None:
            fast = fast.Next
            if i > 0:
                i -= 1
                continue
            slow = slow.Next
        if i == 0:
            return slow.Value
        else:
            return False

    def __str__(self):
        current = self.Head
        res = []
        while current != None:
            res.append(str(current.Value))
            current = current.Next
        return ", ".join(res)


# %%

sample_list = LinkedList()
for i in np.random.randint(1, 10, 20):
    sample_list.InsertBeginning(i)
print(sample_list)
sample_list.remove_dups()
print(sample_list)

# %%
sample_list = LinkedList()
for i in range(10, 20, 1):
    sample_list.InsertBeginning(i)
print(sample_list)
sample_list.ith_element(1)

# %%
sample_list = LinkedList()
for i in range(10, 20, 1):
    sample_list.InsertBeginning(i)
print(sample_list)
sample_list.ith_element_fast_slow(9)


# %%
