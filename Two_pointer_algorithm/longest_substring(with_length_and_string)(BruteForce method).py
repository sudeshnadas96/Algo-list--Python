#to find the length longest substring without repeatition of any character
#Brute-Force Method
def longest_substring(m):
    n = len(m)
    maxlen = 0
    long_sub = "" # an empty list is talken to store the substring"
    for i in range(0 , n):
        empty_set  = set()
        temp_sub = "" # this string stores the current substring we are checking
        for j in range(i , n):
            if m[j] not in empty_set:
                empty_set.add(m[j])
                temp_sub += m[j]
                if len(temp_sub) > maxlen: # checking the length of substring in present iteraion is greater than maxlen or not
                    maxlen = len(temp_sub) # updating the value of maxlen
                    long_sub = temp_sub    # updating the final length to the long_sub
            else:
                break
    print(long_sub) # printing the longest substring
    return maxlen
m = "cadsfrecdsfgt"
print(longest_substring(m))
