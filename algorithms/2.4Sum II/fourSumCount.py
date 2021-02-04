# 454. 4Sum II
# https://leetcode.com/problems/4sum-ii/

# Time complexity: 2*O(N^2) -> O(N^2)
# N is maximum size of the 4 input arrays
# Space complexity: O(N) - due to usage of maps
def fourSumCount(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    ans = 0
    hash_tbl = {}
    for x in A:
        for y in B:
            sumVal = x + y
            if sumVal not in hash_tbl:
                hash_tbl[sumVal] = 1
            else:
                hash_tbl[sumVal] += 1
    
    for x in C:
        for y in D:
            sumVal = -(x + y)
            if sumVal in hash_tbl:
                ans += hash_tbl[sumVal]
    return ans
