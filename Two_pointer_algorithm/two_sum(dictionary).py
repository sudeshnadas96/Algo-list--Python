#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#best merthod is to use dictionary to store the key as numbers and values as indices
def two_sum(nums,target):
    num_dict = {}
    for index,value in enumerate(nums):
        complement = target - value
        if complement in num_dict:
            return (num_dict[complement],index)
        num_dict[value] = index
    return []
nums = [1,3,4,5,6]
target = 7
print(two_sum(nums,target))