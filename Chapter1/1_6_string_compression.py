#String Compression: Implement a method to perform basic string compression
#  using the counts of repeated characters. For example, the string aabcccccaaa 
# would become a2blc5a3. If the "compressed" string would not become smaller than the
#  original string, your method should return the original string. You can assume the
#  string has only uppercase and lowercase letters (a - z). Hints:#92, #110 String
#  Compression: Implement a method to perform basic string compression using the counts of
#  repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
#  "compressed" string would not become smaller than the original string, your method should
#  return the original string. You can assume the string has only uppercase and lowercase 
# letters (a - z). Hints:#92, #110 

# %%

def compress(s):
    new_str = []
    current_str = s[0]
    count = 0
    for c in s:
        if current_str == c:
            count = count +1
        else:
            new_str.append(current_str)
            new_str.append(str(count))
            current_str = c
            count = 1
    new_str.append(current_str)
    new_str.append(str(count))
    res = "".join(new_str)
    if len(res) >= len(s):
        return s
    else:
        return res


        
# %%
compress("A") == "A"
compress("AA") == "A2"
compress("AAA") == "A3"
compress("AAAB") == "AAAB"
compress("AAABB") == "A3B2"
# %%

# %%
# %%