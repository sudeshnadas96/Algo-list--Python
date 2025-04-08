""" 
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3"""

def longest_consecutive_subsequence(m):
    num_set = set(m)
    maxlen = 0
    for num in num_set:
        if num-1 not in num_set:
            current = num
            current_streak = 1


            while current + 1 in num_set:
                current += 1
                current_streak += 1
            maxlen = max(maxlen, current_streak)
    return maxlen
print(longest_consecutive_subsequence([1,0,1,2])) #3
print(longest_consecutive_subsequence([0,3,7,2,5,8,4,6,0,1]))#9