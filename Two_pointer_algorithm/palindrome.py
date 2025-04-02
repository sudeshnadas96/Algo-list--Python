def palindrome(m):
    l = 0   #we take two pointers l and r
    r = len(m) - 1  #setting the value of r to the end of the string
    while l < r:    # running a while loop until l is less than r
        if m[l] != m[r]:
          return False
        l = l + 1 #after checking first and last element , if they are equal we increement l by 1 and r by 1
        r = r - 1
    return True
m = 'madam'
print(palindrome(m))