# 169. Majority Element
# https://leetcode.com/problems/majority-element/

from typing import List

# Time complexity & Space complexity: O(N)
def majorityElement_1(nums: List[int]) -> int:
    hash_tbl = {}
    n = len(nums)
    if n == 1:
        return nums[0]
    for num in nums:
        if num in hash_tbl:
            hash_tbl[num] += 1
            if hash_tbl[num] > n/2:
                return num
        else:
            hash_tbl[num] = 1

# Time complexity & Space complexity: O(2*N) = O(N)
def majorityElement_2(nums: List[int]) -> int:
    hash_tbl = {}
    for num in nums:
        hash_tbl[num] = hash_tbl.get(num, 0) + 1
    
    for num in nums:
        if hash_tbl[num] > len(nums)/2:
            return num
    

if __name__ == "__main__":
    print(majorityElement_1([6,6]))
    print(majorityElement_1([2,2,1,1,1,2,2]))

    print(majorityElement_2([6,6]))
    print(majorityElement_2([2,2,1,1,1,2,2]))