"""Input: arr[]=[1,1,2,2,2,3,3]
Output: [1,2,3,_,_,_,_]
Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.
Input: arr[]=[1,1,1,2,2,3,3,3,3,4,4]
Output: [1,2,3,4,_,_,_,_,_,_,_]
Explanation: Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.

brute force approch is simple just traverse the array and insert elements into a set,a set cant store a duplicate value after traversal of entire array 
just convert set into array or if you want to make changes in original arrray replace set elements in 
array starting from 0 th element and print until size of the set 

time complexity would be o(n)+o(size of set worst case o(n) with no duplicate items in original array also we donot nned to rearrage original array if the size of set is eaquals to size of array)

"""

def remove_duplicates(array):
  i=0
  for j in range (len(array)):
    if array[i]!=array[j]:
      i=i+1
      array[i]=array[j]
  
  return i+1
  
array=[1,1,2,2,2,3,3]
unique_elements=remove_duplicates(array)
print("array after removing duplicates ",array[:unique_elements])
print("count of unique elements",unique_elements)

"""
time complexity o(n)
space complexity o(1)

"""