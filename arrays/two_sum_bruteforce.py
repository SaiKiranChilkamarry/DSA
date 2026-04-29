"""
Problem: Two Sum

Given an array of integers and a target,
return indices of two numbers such that
they add up to the target.


Time Complexity: O(n^2)
Space Complexity: O(1)
"""
"""
Problem: Two Sum

Constraints:
- 2 <= len(arr) <= 10^4
- -10^9 <= arr[i] <= 10^9
- -10^9 <= target <= 10^9
- Exactly one valid solution exists
- Cannot use the same element twice
"""
"Bruteforce approch "

def two_sum_brute(arr,target):
  for i in range (len(arr)):
    for j in range (i+1,len(arr)):
      if arr[i]+arr[j]==target:
        return [i,j]


array = [10, 22, 5, 75, 65, 80, 15, 3, 7]
target = 85
result=two_sum_brute(array,target)
print(result)

"""
Time Complexity = O(n^2)
space complexity = 0(1)

"""







