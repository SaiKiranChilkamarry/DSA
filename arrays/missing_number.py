"""
Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4
"""


def missing(array):
  sum1=0
  n=len(array)+1
  for i in range(n-1):
    sum1=sum1+array[i]
  sum2=n*(n+1)//2
  return sum2-sum1



array= [8, 2, 4, 5, 3, 7, 1]
element = missing(array) 
print("missing number in the given array is ",element)
