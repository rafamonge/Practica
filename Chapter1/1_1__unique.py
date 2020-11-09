# %%

# Notes: the size of the domain of the value is important
# given that they are strings in this case
# if they where  ASCII, you could live with an array of 256 values
# this would make it a O(1) space algorithm
# if the domain ism once again, limied like in this csae to 256
# if the length of the input was longer than the domain, you could discard that.
# with all that in mind, the best possible algorithm is


def unique(str):
    """
    Time: O(N)
    Space: O(N)
    """
    dic = {}
    for c in str:
        if dic.get(c) == None:
            dic[c] = True
        else:
            return False
    return True


def unique_sort(str):
    """
    Time: O(N log(N))
    Space: O(1)
    """
    str = sorted(str)
    for i, c in enumerate(str):
        if i == 0:
            continue
        if c == str[i - 1]:
            return False
    return True


def unique_crappy(str):
    for i, c in enumerate(str):
        for i2, c2 in enumerate(str):
            if c == c2 and i != i2:
                return False
    return True


def unique_less_crappy(str):
    l = len(str)
    for i in range(l):
        for j in range(i + 1, l):
            if str[i] == str[j]:
                return False
    return True


# %%

unique("abcdb")

# %%


unique_sort("ABC")

# %%

unique_crappy("ABCA")

# %%
unique_less_crappy("ADEFGCA")


# %%
