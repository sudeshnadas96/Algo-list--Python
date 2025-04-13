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
"""def binary_subarray(m, goal):
    n = len(m)
    l = 0
    r = 0
    count = 0
    total = 0

    while r < n:
        total += m[r]
        #print(total)

        while total > goal and l <= r:
            total -= m[l]
            l += 1

        # Count all valid subarrays ending at r with sum == goal
        if total == goal:
            temp = l
            while temp <= r and m[temp] == 0:
                count += 1
                temp += 1
            count += 1  # count the base case

        r += 1

    return count"""
def binary_subarray(m, goal):
    def at_most(k):
        if k < 0:
            return 0
        n = len(m)
        l = 0
        total = 0
        count = 0
        for r in range(n):
            total += m[r]
            while total > k:
                total -= m[l]
                l += 1
            count += (r - l + 1)
        return count

    return at_most(goal) - at_most(goal - 1)


print(binary_subarray([1,0,1,0,1] , 2))
print(binary_subarray([0,0,0,0,0] , 0))
print(binary_subarray([1,0,0,1,1,0] , 2))