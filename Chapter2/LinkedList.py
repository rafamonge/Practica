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

    def delete_value(self, value):
        if self.is_empty():
            return
        elif self.Head.Value == value:
            self.Head = self.Head.Next
            return
        current = self.Head
        while current != None:
            if current.Next != None and current.Next.Value == value:
                current.Next = current.Next.Next
                return
            current = current.Next
        return

    def palyndrome(self):
        head = None
        current = self.Head
        while current != None:
            head = Node(current.Value, head)
            current = current.Next

        current = self.Head
        while current != None:
            if current.Value != head.Value:
                return False
            current = current.Next
            head = head.Next
        return True

    def partition(self, part):
        # if self.is_empty():
        # return
        small = None
        small_tail = None
        large = None
        current = self.Head
        while current != None:
            next = current.Next
            if current.Value < part:
                current.Next = small
                small = current
                if small_tail is None:
                    small_tail = current
            else:
                current.Next = large
                large = current
            current = next
        if small is None:
            self.Head = large
        else:
            small_tail.Next = large
            self.Head = small

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
sample_list = LinkedList()
for i in range(10, 20, 1):
    sample_list.InsertBeginning(i)
print(sample_list)
print(sample_list)


# %%
sample_list = LinkedList()
for i in np.random.randint(1, 20, 30):
    sample_list.InsertBeginning(i)
# print(sample_list)
sample_list.partition(12)
print(sample_list)

# %%

sample_list = LinkedList()
for i in range(1, 5, 1):
    sample_list.InsertBeginning(i)
# for i in range(4, 0, -1):
# sample_list.InsertBeginning(i)
print(sample_list)
sample_list.palyndrome()
# print(sample_list)


# %%
def sum_lists(l1, l2):
    carryover = 0
    current_l1 = l1.Head
    current_l2 = l2.Head
    result = LinkedList()
    while current_l1 != None or current_l2 != None or carryover > 0:
        val_l1 = current_l1.Value if current_l1 != None else 0
        val_l2 = current_l2.Value if current_l2 != None else 0
        total = val_l1 + val_l2 + carryover
        digit = total % 10
        carryover = int((total - digit) / 10)
        result.InsertBeginning(digit)
        current_l2 = current_l2.Next if current_l2 != None else None
        current_l1 = current_l1.Next if current_l1 != None else None
    current = result.Head
    new_res = LinkedList()
    while current != None:
        new_res.InsertBeginning(current.Value)
        current = current.Next
    return new_res


def sum_lists_recur(l1, l2):
    return sum_lists_aux(l1.Head, l2.Head, 0)


def sum_lists_aux(l1, l2, carry):
    if l1 == None and l2 == None:
        res = LinkedList()
        if carry != 0:
            res.InsertBeginning(carry)
        return res
    ## we have values in the lists:
    val_l1 = l1.Value if l1 != None else 0
    val_l2 = l2.Value if l2 != None else 0
    total = val_l1 + val_l2 + carry
    digit = total % 10
    carry = int((total - digit) / 10)
    l2 = l2.Next if l2 != None else None
    l1 = l1.Next if l1 != None else None
    res = sum_lists_aux(l1, l2, carry)
    res.InsertBeginning(digit)
    return res


l1 = LinkedList()
l1.InsertBeginning(1)
# l1.InsertBeginning(9)
# l1.InsertBeginning(9)
l2 = LinkedList()
l2.InsertBeginning(9)

print(sum_lists(l1, l2))


# %%
# %%
# %%

