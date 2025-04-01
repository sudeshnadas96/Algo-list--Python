#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#best merthod is to use dictionary to store the key as numbers and values as indices
def two_sum(nums,target):
    num_dict = {}
    for index,value in enumerate(nums): #the enumerate method will give the index and value of the list
        complement = target - value     # we subtract and check for the result
        if complement in num_dict:
            return (num_dict[complement],index) #if the subtracted value is already present in dictionary than we return the present value index and the index of the subtracted value that is already present in the dictionary
        num_dict[value] = index #if the complement is not in dictionary , we will store the value as key and index as value in the dictionary
    return []
nums = [1,3,4,5,6]
target = 7
print(two_sum(nums,target))