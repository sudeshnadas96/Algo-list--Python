#longest subarray with sum <= k, here k is given number
#Bruteforce method
def longest_substring(m,k):
    n = len(m)
    maxlen = 0
    for i in range(0, n-1):
        total_sum = 0
        for j in range(i, n-1):
            total_sum = total_sum + m[j]
            if total_sum <= k:
                maxlen = max(maxlen, j-i+1)
            elif (total_sum > k):
                break
    return maxlen
m = [2,5,1,7,10]
k = 14
print(longest_substring(m,k))
