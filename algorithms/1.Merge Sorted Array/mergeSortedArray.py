# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

# Note: do not use built-in sort() function 
import heapq
import time

def merge(nums1, m, nums2, n):
    m -= 1
    n -= 1
    while m >= 0 and n >= 0:
        if nums1[m] >= nums2[n]:
            nums1[m + n + 1] = nums1[m]
            m -= 1
        else:
            nums1[m + n + 1] = nums2[n]
            n -= 1
    if n >= 0:
        nums1[:n+1] = nums2[:n+1]

def merge_using_traverse(nums1, m, nums2, n):
    nums3 = [None]*(m+n)
    i, j, k = 0, 0, 0

    # Traverse both array
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            nums3[k] = nums1[i]
            k += 1
            i += 1
        else:
            nums3[k] = nums2[j]
            k += 1
            j += 1
    # Store the remaining elements 
    while i < m:
        nums3[k] = nums1[i]
        k += 1
        i += 1
    while j < n:
        nums3[k] = nums2[j]
        k += 1
        j += 1    

    return nums3

def merge_using_heapq(nums1, m, nums2, n):
    nums1 = list(filter(lambda num: num != 0, nums1))
    nums2 = list(filter(lambda num: num != 0, nums2))
    return list(heapq.merge(nums1, nums2))

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    start_time = time.time()
    res_func1 = merge_using_traverse(nums1, m, nums2, n)
    print(res_func1)
    print(time.time() - start_time)

    start_time = time.time()
    res_func2 = merge_using_heapq(nums1, m, nums2, n)
    print(res_func2)
    print(time.time() - start_time)
    
    print("Check: res_func1 is same as res_func2 -> " + str(res_func1 == res_func2))


