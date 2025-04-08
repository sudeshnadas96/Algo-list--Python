"""You are given a string 'str' and an integer ‘K’. Your task is to find the length of the largest substring with at most ‘K’ distinct characters.

For example:
You are given ‘str’ = ‘abbbbbbc’ and ‘K’ = 2, then the substrings that can be formed are [‘abbbbbb’, ‘bbbbbbc’]. Hence the answer is 7."""
#Brute force

def distinct_substring(s , k):
    n = len(s)
    maxlen = 0
    string_dict = {}
    for i in range(n):
        for j in range(i+1 , n):
            if s[j] not in string_dict:
                string_dict[s[j]] = 1
            else:
                string_dict[s[j]] += 1
            if len(string_dict) <= k:
                maxlen = max(maxlen , j-i+1)
            else:
                break
    return maxlen
print(distinct_substring("aaabbbcc",2))