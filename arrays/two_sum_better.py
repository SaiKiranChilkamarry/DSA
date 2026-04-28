"""Problem: Two Sum

Given an array of integers and a target,
return indices of two numbers such that
they add up to the target.
Constraints:
- 2 <= len(arr) <= 10^4
- -10^9 <= arr[i] <= 10^9
- -10^9 <= target <= 10^9
- Exactly one valid solution exists
- Cannot use the same element twice

Hash approch 
"""
def two_sum_hash_approch(array,target):
  hashmap={}
  for i in range(len(array)):
    compliment = target-array[i]
    if compliment in hashmap:
      return[i,hashmap[compliment]]
    else:
      hashmap[array[i]]=i
    
    
array = [10, 22, 5, 75, 65, 80, 15, 3, 7]
target = 85
result=two_sum_hash_approch(array,target)
print(result)