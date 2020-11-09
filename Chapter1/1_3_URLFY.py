# %%
from array import array

test = "ABC DEF GHI"
test_res = "ABC%20DEF%20GHI"
test = "ABC DEF GHI                 "

#       01234567890123456789
test = "ABC DEF GHI                 "
# %%
def urlfy_dummy(s1):
    array = s1.split(" ")
    return "%20".join(array)


"A%20B"
# %%
def urlfy_assuming_c_like_array(s1, true_length):
    offset = 0
    s1 = list(s1)
    for i in range(true_length):
        if s1[i + offset] == " ":
            shift_right(s1, i, offset, true_length)
            offset += 2
    return str(s1)


def shift_right(ss, i, offset, true_length):
    start = i + offset
    end = true_length + offset + 2
    rango = range(end, start + 2, -1)
    print(list(rango))
    for r in rango:
        # print(ss)
        ss[r] = ss[r - 2]
    ss[start] = "%"
    ss[start + 1] = "2"
    ss[start + 2] = "0"


# %%
