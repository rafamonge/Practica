# %%

from collections import defaultdict

# %%
def palyndrome_permutation_dict(s):
    d = defaultdict(lambda: 0)
    for c in s:
        if c == " ":
            continue
        d[c] = d[c] + 1
    return check_dict(d)


def check_dict(dd):
    seen_odd = False
    for v in dd.values():
        if v % 2 == 0:
            continue
        elif seen_odd == False:
            seen_odd = True
        else:
            return False
    return True




# %%
palyndrome_permutation_dict("COTAOOCATT")

# %%

