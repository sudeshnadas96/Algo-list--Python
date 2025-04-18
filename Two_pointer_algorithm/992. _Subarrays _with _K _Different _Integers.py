#992. Subarrays with K Different Integers(Brute Force)
"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
"""
def Subarrays_with_k_different_integers(nums , k):
    n = len(nums)
    count = 0
    for i in range(n):
        empty_set = set()
        for j in range(i , n):
            empty_set.add(nums[j])
            if len(empty_set) == k:
                count = count + 1
    return count
print(Subarrays_with_k_different_integers([1,2,1,2,3] , 2)) #7
print(Subarrays_with_k_different_integers([1,2,1,3,4] , 3)) #3