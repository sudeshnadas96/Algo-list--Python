#to find the longest substring where sum<=k
def longest_substring(m, k):
    n = len(m)
    l = 0  #initialized pointer l, it will start from 0
    r = 0  #initialized pointer r, it will also point at 0
    total_sum = 0 #initialized total_sum
    maxlen = 0    #initialized maxlength
    while(r < n):  #running while loop unitil l<r
        total_sum = total_sum + m[r] #keep on adding the new element at r position in list m
        while(total_sum > k):        # running while loop for totalsum > k
            total_sum = total_sum - m[l] # if sum>k, we delete the first element and increment l
            l = l + 1                    # we are shrinking the window from the left side
        if total_sum <= k:               # checking if totalsum is less than k
            maxlen = max(maxlen, r-l+1)  # updating the maxlen
        r = r + 1                        # incrementing r by 1
    return maxlen
m = [1,3,10,10]
k = 4
print(longest_substring(m, k))