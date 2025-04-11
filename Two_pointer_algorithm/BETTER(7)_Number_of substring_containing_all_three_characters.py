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
"""

1) We start from storing the index of the characters in a hash
2) for "bbacba":
-  a = -1, b = -1, c = -1
-  start iterating and updating index:
   -  a = -1, b = 0, c = -1
   -  a = -1, b = 1, c = -1
   -  a = 2, b = 1, c = -1
   -  a = 2, b = 1, c = 3
- Now we have all three: "bac" is a valid substring(count = 1)
- Now all the other characters on the left of "b" can be added (count = 1+1 = 2)
- Move the pointer from c to b i.e a = 2, b = 4, c = 3 (a has the smallest index, so "acb" is the string)(count = 2+1=3)
- keep on adding the left i.e 2+1+1+1 = 5
- we move the pointer to "a" i.e. a = 5,b = 4, c = 3 (c has the smallest index so : "cba"-> count = 5 + 1 = 6)
- we add the left side characters of c i.e (5 + 1+ 1 + 1 = 8)
 
"""
def string_count_having_all_three_character(string):
    n = len(string)
    lastseen = {'a': -1, 'b': -1, 'c': -1}  # Stores last index seen for 'a', 'b', and 'c'
    count = 0

    for i in range(n):
        if string[i] in lastseen:
            lastseen[string[i]] = i  # Update last seen index for current character

        if -1 not in lastseen.values():  # Check if all three characters have been seen at least once
            count += 1 + min(lastseen.values())  # Count substrings ending at i that include all 3 characters

    return count

      
print(string_count_having_all_three_character('abccabc'))