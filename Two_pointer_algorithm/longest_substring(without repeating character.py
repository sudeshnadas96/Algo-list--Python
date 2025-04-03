#to find the length longest substring without repeatition of any character
def longest_substring(m):
    n = len(m)
    maxlen = 0
    for i in range(0,n): # run a loop till the end of the list
        empty_set = set() #we use the set datastructure to store the elements
        
        for j in range(i,n): # this for loop checkseach element from first index to last index
            
            if m[j] not in empty_set: # if the element is not present in the set, we add the element 
                empty_set.add(m[j])
                
                maxlen = max(maxlen , j - i + 1) #check the  the maximum length of longest substring
                
                
            else:
                break  # if element is already there we break the loop
    
    return maxlen      # we return the maxlength of the substring without repeatition
m = 'cadbghtcbdes'
print(longest_substring(m))