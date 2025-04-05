"""You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length"""
def total_fruits(trees , k):
    n = len(trees)
    l = 0
    r = 0
    maxlen = 0
    type_frequency = {}
    while(r < n):
        if trees[r] not in type_frequency:
            type_frequency[trees[r]] = 1
        else:
            type_frequency[trees[r]] += 1
        if len(type_frequency) > k:
            type_frequency[trees[l]] -= 1 #decreasing the value of key by 1
            if type_frequency[trees[l]] == 0:
                type_frequency.pop(trees[l]) #if value = 0, we delete the key
            l = l + 1
        if len(type_frequency) <= k:
            maxlen = max(maxlen, r - l + 1)
        r = r + 1
    return maxlen
print(total_fruits([1,2,1] , 2))
print(total_fruits([0,1,2,2] , 2))
print(total_fruits([1,2,3,2,2] , 2))

            
