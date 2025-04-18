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
def subarray_with_k_diff_int(nums , k):
    def count_atmost(goal):
        if goal < 0:
            return 0
        n = len(nums)
        l = 0
        r = 0
        count = 0
        subarray_dict = {}
        while(r < n):
            if nums[r] in subarray_dict:
                subarray_dict[nums[r]] += 1
            else:
                subarray_dict[nums[r]] = 1
            while(len(subarray_dict) > goal):
                subarray_dict[nums[l]] -= 1
                if subarray_dict[nums[l]] == 0:
                    subarray_dict.pop(nums[l])
                l = l + 1
            if len(subarray_dict) <= goal:
                count = count + (r -l + 1)
            r = r + 1
        return count
    return count_atmost(k) - count_atmost(k - 1)
print(subarray_with_k_diff_int([1,2,1,3,4] , 3)) #3
print(subarray_with_k_diff_int([1,2,1,2,3] , 2)) #7
print(subarray_with_k_diff_int([1,2,1,2,3] , 0)) #0
