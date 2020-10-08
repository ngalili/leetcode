# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List

# solution 1
def findKthLargest_1(nums: List[int], k: int) -> int:
    lst = sorted(nums, reverse=True)
    return lst[k-1]

# solution 2 - referred to Internet resources 
from random import randint
def findKthLargest_2(nums: List[int], k: int) -> int:
    res = quickSort(nums, k)
    try:
        return res[0]
    except:
        return res
def quickSort(nums, k):
    n = len(nums)
    if len(nums) < 2:
        return nums
    
    lower, same, higher = [],[],[]
    pivot = nums[randint(0, n-1)]
    
    for item in nums:
        if item < pivot:
            lower.append(item)
        elif item == pivot:
            same.append(item)
        else:
            higher.append(item)
    if k <= len(higher):
        return quickSort(higher, k)
    elif k > (len(higher) + len(same)):
        return quickSort(lower, k-len(higher)-len(same))
    else:
        return pivot
    
if __name__ == "__main__":
    print(findKthLargest_1([3,2,1,5,6,4], 2))
    print(findKthLargest_2([3,2,1,5,6,4], 2))