# 220. Contains Duplicate III
# https://leetcode.com/problems/contains-duplicate-iii/

# not clearly understand
def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
    if t < 0:
        return False
    n = len(nums)
    d = {}
    w = t+1
    for i in xrange(n):
        m = nums[i]/w
        if m in d:
            return True
        if m - 1 in d and abs(nums[i] - d[m-1]) < w:
            return True
        if m + 1 in d and abs(nums[i] - d[m+1]) < w:
            return True
        d[m] = nums[i]
        if i >= k: del d[nums[i-k]/w]
    return False