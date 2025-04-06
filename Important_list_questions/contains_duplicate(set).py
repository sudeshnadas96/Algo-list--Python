def contains_duplicate(nums):
    n = len(nums)
    empty_set = set()
    for i in range(n):
        if nums[i] in empty_set:
            return True
        empty_set.add(nums[i])
    return False
print(contains_duplicate([2,2,3,4,5]))
print(contains_duplicate([1,3,4,5]))
print(contains_duplicate([1,3,4,5,5]))

