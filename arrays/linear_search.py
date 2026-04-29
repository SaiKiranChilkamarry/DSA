"""Example 1:
Input:
 arr[] = 1 2 3 4 5, num = 3  
Output:
 2  `
Explanation:
 3 is present at the 2nd index of the array.

Example 2:
Input:
 arr[] = 5 4 3 2 1, num = 5  
Output:
 0  
Explanation:
 5 is present at the 0th index of the array.
 """


def linear_search(array,target):

  for i in range(len(array)):
    if array[i]==target:
      return i
  return -1  




array=[31,24,32,14,5]
target=14
result=linear_search(array,target)
if result == -1:
  print("target not found ")
else :
  print("target found at index",result)


#linear search algorithm 
"timecomplexity o(n),space complexity o(1)"