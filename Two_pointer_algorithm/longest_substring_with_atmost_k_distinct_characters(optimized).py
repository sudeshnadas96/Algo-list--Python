"""You are given a string 'str' and an integer ‘K’. Your task is to find the length of the largest substring with at most ‘K’ distinct characters.

For example:
You are given ‘str’ = ‘abbbbbbc’ and ‘K’ = 2, then the substrings that can be formed are [‘abbbbbb’, ‘bbbbbbc’]. Hence the answer is 7."""
# important question

def distinct_character(s,k):
    n = len(s)
    l = 0
    r = 0
    maxlen = 0
    char_dict = {}
    while(r < n):
        if s[r] not in char_dict:
            char_dict[s[r]] = 1
        else:
            char_dict[s[r]] += 1
        if len(char_dict) > k:
            char_dict[s[l]] -= 1
            if s[l] == 0:
                char_dict.pop(s[l])
            l = l + 1
        if len(char_dict) <=k:
            maxlen = max(maxlen, r-l+1)
        r = r + 1
    return maxlen
print(distinct_character("aaabbbc" , 2)) #6
