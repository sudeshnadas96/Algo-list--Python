def contains_duplicate(nums):
    return len(set(nums)) != len(nums)
print(contains_duplicate([2,2,3,4,5]))
print(contains_duplicate([1,3,4,5]))
print(contains_duplicate([1,3,4,5,5]))
