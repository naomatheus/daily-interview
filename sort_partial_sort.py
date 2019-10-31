# You are given a list of n numbers,
# where every number is at most k indexes away from its properly sorted index. Write a sorting algorithm (that will be given the number k) for this list that can solve this in O(n log k)

# Example:
# Input: [3, 2, 6, 5, 4], k=2
# Output: [2, 3, 4, 5, 6]

# As seen above, every number is at
# most 2 indexes away from its proper
# sorted index.

# Here's a starting point:

def sort_partially_sorted(list, k):
 # Fill this in
    print('splitting...')
    
    if len(list) > 1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]
    print(lefthalf,righthalf)

# recursion
    sort_partially_sorted(lefthalf,2)
    sort_partially_sorted(righthalf,2)

    i=0
    j=0
    k=0
    new_list = []
    while i < len(lefthalf) and j > len(righthalf):
    # while split lists are > 0 length
    # compare each of the elements and group them
        if lefthalf[i] < righthalf[j]:
            new_list[k]=lefthalf[i]
            i=i+1
        else:
            new_list[k]=righthalf[j]
            j=j+1
            k=k+1
    while i < len(lefthalf):
        new_list[k] = lefthalf[i]
        i=i+1
        k=k+1
    while j < len(righthalf):
        new_list[k]=righthalf[j]
        j=j+1
        k=k+1
    
    print('merging...',new_list)

     

    sort_partially_sorted(list)

print(sort_partially_sorted([3, 2, 6, 5, 4],2))
# [2,3,4,5,6]