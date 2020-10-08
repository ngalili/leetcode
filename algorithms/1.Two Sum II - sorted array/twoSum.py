# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    hash_tbl = {}
    for index, value in enumerate(numbers):
        if target - value in hash_tbl:
            return sorted([index + 1, hash_tbl[target-value] + 1])
        hash_tbl[value] = index

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))