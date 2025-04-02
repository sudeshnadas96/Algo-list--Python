def longest_substring(m, k):
    n = len(m)
    l = 0
    r = 0
    total_sum = 0
    maxlen = 0
    while(r < n):
        total_sum = total_sum + m[r]
        while(total_sum > k):
            total_sum = total_sum - m[l]
            l = l + 1
        if total_sum <= k:
            maxlen = max(maxlen, r-l+1)
        r = r + 1
    return maxlen
m = [1,3,10,10]
k = 4
print(longest_substring(m, k))