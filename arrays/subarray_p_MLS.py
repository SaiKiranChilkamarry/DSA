# longest sub array with sum k Better Approch Approch (positive integers) 


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
        hashmap[prefix_sum]=i
    return max_length

array=[1,2,3,1,1,1,14,2,3]
k=3
result = find_subarray(array,len(array),k)
print ("length of the longest subarray is ",result )