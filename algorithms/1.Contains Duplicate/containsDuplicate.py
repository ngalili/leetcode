# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

from typing import List

# Time limit exceeded when Big test data is checked
def containsDuplicate_1(nums: List[int]) -> bool:
    m = []
    for num in nums:
        if num in m:
            return True
        m.append(num)
    return False

# size checking
def containsDuplicate_2(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

# using hash table 
# Time complexity and Space complexity: O(N)
def containsDuplicate_3(nums: List[int]) -> bool:
    hash_tbl = {}
    for num in nums:
        if num in hash_tbl:
            return True
        hash_tbl[num] = 1
    return False

# using defaultdict 
from collections import defaultdict
def containsDuplicate_4(nums: List[int]) -> bool:
    m = defaultdict(int)
    for num in nums:
        if m[num]:
            return True
        m[num] += 1
    return False

# using sorted func 
def containsDuplicate_5(nums: List[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

if __name__ == "__main__":
    print(containsDuplicate_1([1,1,1,3,3,4,3,2,4,2]))
    print(containsDuplicate_2([1,1,1,3,3,4,3,2,4,2]))
    print(containsDuplicate_3([1,1,1,3,3,4,3,2,4,2]))
    print(containsDuplicate_4([1,1,1,3,3,4,3,2,4,2]))
    print(containsDuplicate_5([1,1,1,3,3,4,3,2,4,2]))

