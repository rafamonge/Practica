# %%


def one_away(s1, s2):
    difference = len(s1) - len(s2)
    print(difference)
    if difference == 0:
        return one_away_replace_aux(s1, s2)
    elif difference == 1:
        return one_away_diff(s1, s2)
    elif difference == -1:
        return one_away_diff(s2, s1)
    else:
        return False


def one_away_replace_aux(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count = count + 1
            if count > 1:
                return False
    return True


def one_away_diff(big, small):
    big_i = 0
    small_i = 0
    while big_i < len(big) and small_i < len(small):
        if big[big_i] == small[small_i]:
            big_i += 1
            small_i += 1
        elif big_i - small_i == 1:
            return False
        else:
            big_i += 1
    return big_i - small_i < 2


# %%

