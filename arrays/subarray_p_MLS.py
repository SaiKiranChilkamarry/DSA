"""Example 1:
Input:
 nums = [10, 5, 2, 7, 1, 9], k = 15 (assuming only possitive integers in an array) 
Output:
 4  
Explanation:
 The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.


 0  
Explanation:
 There is no sub-array in the array that sums to 6. Therefore, the output is 0.
"""

"""
its a better approch then the brute force approch we initially finished 
Time complexity=o(n)
space complexity=O(n) for hashmap 
 
"""


def find_subarray(array,n,k):
    hashmap={}
    prefix_sum=0
    max_length=0
    for i in range (n):
        prefix_sum=prefix_sum+array[i]
        find=prefix_sum-k
        if prefix_sum==k:
            max_length=max(max_length,i+1)
        if find in hashmap:
            length = i - hashmap[find]
            max_length=max(max_length,length)
        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = i
    return max_length

array=[1,2,3,1,1,1,14,2,3]
k=3
result = find_subarray(array,len(array),k)
print ("length of the longest subarray is ",result )