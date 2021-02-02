# 1. Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List

# simplest algorithm
def twoSum_1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

# optimized algorithm - referred to Internet resources: using hash table 
def twoSum_2(nums: List[int], target: int) -> List[int]:
    hash_tbl = {}
    for index, value in enumerate(nums):
        if target - value in hash_tbl:
            return sorted([index, hash_tbl[target-value]])
        hash_tbl[value] = index

if __name__ == "__main__":
    print(twoSum_1([2,7,11,15], 9))
    print(twoSum_2([2,7,11,15], 9))


