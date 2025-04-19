#76. Minimum Window Substring
"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""
def min_window_substring(s , t):
    n = len(s)
    m = len(t)
    l = 0
    r = 0
    sindex = -1
    minlen = 10**9
    count = 0
    t_dict = {}
    # insert t chars and their freq
    for i in range(m):
        if t[i] in t_dict:
            t_dict[t[i]] += 1
        else:
            t_dict[t[i]] = 1
    while(r < n):
        # Freq greater than 0 denotes there is one match with t characters with s characters
        if s[r] in t_dict:
            if t_dict[s[r]] > 0:
                count = count + 1
            t_dict[s[r]] -= 1
        
        # if count is equal to m keep shrinking and update states like minLen, sIndex, t_dict and count
        while (count == m):
            if (r - l + 1 < minlen):
                minlen = r - l + 1
                sindex = l
            # check if s[l] exist in t_dict
            if s[l] in t_dict:
                t_dict[s[l]] += 1
                if  t_dict[s[l]] > 0:
                    count = count - 1
            l = l + 1
        r = r + 1
    if sindex == -1:
       return ""
    else:
        return s[sindex : sindex + minlen]
print(min_window_substring("ADOBECODEBANC" ,  "ABC")) 
print(min_window_substring("a", "aa"))
print(min_window_substring("a", "a"))
print(min_window_substring("a", "b"))


       
