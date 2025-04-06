#Given an array of integer(nums) and an integer (target) , return indices of the two numbers such that they add upto target.
def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i , j)
print(two_sum([1 , 2 ,3 ,4] , 5))
