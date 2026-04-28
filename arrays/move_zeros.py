"""Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
Input : 1,2,0,1,0,4,0
Output: 1,2,1,4,0,0,0
Explanation : All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
"""
def move_zeros(array):
    i = 0
    for j in range(len(array)):
        if array[j] != 0:
            array[i], array[j] = array[j], array[i]
            i += 1
    return array

array=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
move_zeros(array)

"""
time complexity o(n)
"""