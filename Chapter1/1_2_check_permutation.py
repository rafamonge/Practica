# %%

from collections import defaultdict


# %%


def permutation_sort(s1, s2):
    """
    Time: N log N
    Space: 1
    """
    return sorted(s1) == sorted(s2)


def permutation_dict(s1, s2):
    """
    Time: N
    Space: N
    """
    d = {}
    if len(s1) != len(s2):
        return False
    for c in s1:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    for c in s2:
        if c in d and d[c] >= 1:
            d[c] = d[c] - 1
        else:
            return False
    return True


def permutation_default_dict(s1, s2):
    """
    Time: N
    Space: N
    """
    if len(s1) != len(s2):
        return False
    d = defaultdict(lambda: 0)
    for c in s1:
        d[c] = d[c] + 1
    for c in s2:
        if d[c] == 0:
            return False
        d[c] = d[c] - 1
    return True


# %%
permutation_sort("ABC", "CBAA")
# %%
permutation_dict("ABCDEF", "BCDEFB")
# %%
permutation_default_dict("ABCCCC", "BCACCA")
# %%
# %%
# %%
