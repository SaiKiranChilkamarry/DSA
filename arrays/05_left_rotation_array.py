"""Input : nums = [1, 2, 3, 4, 5, 6, 7], k = 2, right
Output : [6, 7, 1, 2, 3, 4, 5]
Explanation : rotate 1 step to the right: [7, 1, 2, 3, 4, 5, 6]
rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5] 

Input : nums = [1, 2, 3, 4, 5, 6], k=2, left
Output : [3, 4, 5, 6, 1, 2]
Explanation :rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]
"""
def left_rotation(array,n,k):
  k=k%n
  if k==0:
    return 
  temp=[]
  for i in range (k):
    temp.append(array[i])
  for i in range(k,n):
    array[i-k]=array[i]
  for i in range(len(temp)):
    array[n-k+i]=temp[i]
  


array = [1, 2, 3, 4, 5, 6, 7]
k=43
left_rotation(array,len(array),k)
print(array)

"""
time complexity o(n)+o(k)
space complexity o(k) 
"""