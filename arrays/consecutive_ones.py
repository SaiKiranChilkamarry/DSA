
def max_count_ones(prices):
  maxcount=0
  count=0
  for i in range(len(prices)):
    if prices[i]==1:
      count+=1
      maxcount=max(count,maxcount)
    else:
      count=0
  return maxcount


prices = [1, 1, 0, 1, 1, 1]
result=max_count_ones(prices)
print("the maximum number of consecutive ones in the prices array is/are",result)

"""
time complexity o(n)
"""