#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#brute-force method
#time complexity is O(n**2), for larger list, it will take more time
def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1 , n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return()
nums = [1,3,4,5,6]
target = 7
print(two_sum(nums,target)) #[0,4]

