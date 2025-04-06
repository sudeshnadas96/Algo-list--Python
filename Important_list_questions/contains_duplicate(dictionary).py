# Given an integer array(nums) , return True if any value appears twice in the array and return false if every item is distinct
def contains_duplicate_numbers(nums):
    n = len(nums)
    number_freq = {}
    for i in range(n):
        if nums[i] in number_freq:
            number_freq[nums[i]] += 1
        else:
            number_freq[nums[i]] = 1
    for value in number_freq.values():
        if value >= 2:
            return True
    return False
print(contains_duplicate_numbers([2,2,3,4,5]))
print(contains_duplicate_numbers([1,3,4,5]))
print(contains_duplicate_numbers([1,3,4,5,5]))


