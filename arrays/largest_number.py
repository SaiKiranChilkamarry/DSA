"""Example 1:
Input:
 arr[] = {2, 5, 1, 3, 0}  
Output:
 5  
Explanation:
  
5 is the largest element in the array.

Example 2:
Input:
 arr[] = {8, 10, 5, 7, 9}  
Output:
 10  
Explanation:
  
10 is the largest element in the array.

Brute force approch => sort array return last element 

program for better approch
"""
def find_largest(array):
  if not len(array):
    print ("array is empty")
    return None 
  largest=array[0]
  for i in range(1,len(array)):
    if array[i]>largest:
      largest=array[i]
  return largest 


array= [2, 5, 1, 3, 0]
Largest=find_largest(array)
print("the largest number in the array found is  ",Largest)


"""
time complexity O(n)
space complexity O(1)

"""