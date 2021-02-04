# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

# using hash table - faster than using defaultdict 
def containsNearbyDuplicate_1(nums: List[int], k: int) -> bool:
    dic = {}
    for i, num in enumerate(nums):
        if num in dic and i - dic[num] <= k:
            return True
        dic[num] = i
    return False

# using defaultdict
from collections import defaultdict

def containsNearbyDuplicate_2(nums: List[int], k: int) -> bool:
    m = defaultdict(int)
    for i, num in enumerate(nums):
        if num in m and i - m[num] <= k:
            return True
        m[num] = i
    return False

