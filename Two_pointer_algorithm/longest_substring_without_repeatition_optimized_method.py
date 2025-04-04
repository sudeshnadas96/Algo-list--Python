def longest_substring(m):
    n = len(m)
    l = 0
    r = 0
    maxlen = 0
    empty_set = set()
    long_sub = ""
    while(r < n):
        if m[r] in empty_set:
            empty_set.discard(m[l])
            l = l + 1

        if m[r] not in empty_set:
            empty_set.add(m[r])
            temp_string = m[l : r + 1]
            if len(temp_string) > maxlen:
                maxlen = len(temp_string)
                long_sub = temp_string
        r = r + 1
    print(long_sub)    
    return maxlen

m = 'bcdefghbcd'
print(longest_substring(m))