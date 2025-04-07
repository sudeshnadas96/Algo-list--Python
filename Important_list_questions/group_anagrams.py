"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]"""


def group_anagram(string):
    anagram_dict = {}
    for word in string:
        sorted_word = ' '.join(sorted(word)) # sorted will sort the word and join will join back the sorted word
        if sorted_word in anagram_dict:      #if the word is there, we will append in the list of values
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word] #if the word is not there, we will insert the word in dictionary as a value
    return list(anagram_dict.values())
print(group_anagram(["eat","tea","tan","ate","nat","bat"])) #[["bat"],["nat","tan"],["ate","eat","tea"]]
