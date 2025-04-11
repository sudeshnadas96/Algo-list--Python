"""Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 
"""




def stringcount(string):
    n = len(string)
    count = 0
    for i in range(n):
        string_set = set()
        
        for j in range(i , n):
            string_set.add(string[j])
            #print(string_set)
            if len(string_set) == 3:
                count = count+1
    return count
print(stringcount("abcabc")) #10