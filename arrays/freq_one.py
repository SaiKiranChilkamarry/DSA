"""Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.


Example 2:
Input Format: arr[] = {4,1,2,1,2}
Result: 4
Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.
"""

def frequency(array):
  freq={}
  for num in array:
    freq[num]=freq.get(num,0)+1

  for key,value in freq.items():
    if value == 1:
      return key 



array=[4,1,2,1,2]
result = frequency(array)
print("the element that appears only once in an array is ",result)
"""
time complexity o(n)
space complexity o(n)

we can optimise space complexity using XOR as any number XOR to itself will be zero and element xor with zero would be that element itself\
so here space complexity will be o(1) where time complexity remains o(n)
"""