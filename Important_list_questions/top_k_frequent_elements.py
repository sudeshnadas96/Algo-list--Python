#given an integer array (nums) and an integer k, return most frequently appearing elements within array
def top_k_freq_elements(nums, k):
    elem_dict = {}
    for elem in nums:
        if elem in elem_dict:
            elem_dict[elem] += 1
        else:
            elem_dict[elem] = 1
    sorted_elem_dict = sorted(elem_dict.items(), key = lambda x : x[1], reverse = True)
    result = []
    for i in range(min(k , len(sorted_elem_dict))):
        result.append((sorted_elem_dict[i][0] , "occurs", sorted_elem_dict[i][1], "times"))
    return result
print(top_k_freq_elements([1, 2, 2, 3, 3, 3], 2))
