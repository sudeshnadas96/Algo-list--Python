#To find the maxsum
# k is the length of consecutive numbers in list
def constant_window(m,k):
    n = len(m)
    l = 0
    r = k - 1
    for i in range(l,r+1):
        total_sum = sum(m[l:r+1])
        maxsum = total_sum
    while(r < n-1):
        total_sum = total_sum - m[l]
        l = l +1
        r = r + 1
        total_sum = total_sum + m[r]
        maxsum = max(maxsum, total_sum)
    return maxsum

m = [-1,2,3,4,5,6,-1]
k = 4
print(constant_window(m,k))