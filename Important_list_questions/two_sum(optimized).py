def two_sum(nums , target):
    n = len(nums)
    my_dict = {}
    for index,value in enumerate(nums):
        complement = target - value
        if complement in my_dict:
            return (my_dict[complement] , index)
        my_dict[value] = index
    return []
print(two_sum([2, 3, 4, 5], 7))

