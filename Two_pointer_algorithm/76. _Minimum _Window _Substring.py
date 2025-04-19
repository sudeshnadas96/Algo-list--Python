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
    minlen = 10**9
    sindex = -1
    for i in range(n):
        t_dict = {}
        count = 0
        for j in range(m):
            if t[j] in t_dict:
                t_dict[t[j]] += 1
            else:
                t_dict[t[j]] = 1
        for j in range(i , n):
            if s[j] in t_dict and t_dict[s[j]] > 0:
                count = count + 1
            if s[j] in t_dict:
                t_dict[s[j]] -= 1
            else:
                t_dict[s[j]] = -1
            if count == m:
                if(minlen > j - i + 1):
                    minlen = j - i + 1
                    sindex = i
                    break
    return s[sindex : sindex + minlen]

print(min_window_substring("ADOBECODEBANC" ,  "ABC")) #BANC