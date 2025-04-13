"""930. Binary Subarrays With Sum
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
"""
def binary_subarray(m , goal):
    n = len(m)
    count = 0
    for i in range(n):
        bit_count = {}
        for j in range(i , n):
            if m[j] in bit_count:
                bit_count[m[j]] += 1
            else:
                bit_count[m[j]] = 1
            if bit_count.get(1 , 0) == goal:
                count = count + 1
    return count
print(binary_subarray([1,0,1,0,1] , 2)) #4
print(binary_subarray([0,0,0,0] , 0)) #10