# 1099. Two Sum Less Than K
# https://leetcode.com/problems/two-sum-less-than-k/

from typing import List

# simplest algorithm
def twoSumLessThanK_1(A: List[int], K: int) -> int:
    max_s = -1
    for i in range(len(A)):
        for j in range(i,len(A)):
            tmp = A[i] + A[j]
            if tmp < K and i != j:
                max_s = max(max_s, tmp)
    return max_s

# optimized algorithm
def twoSumLessThanK_2(A: List[int], K: int) -> int:
    lo = 0
    hi = len(A) -1
    A.sort()
    max_s = -1
    while lo < hi:
        if A[lo] + A[hi] < K:
            max_s = max(max_s, A[lo] + A[hi])
            lo += 1
        else:
            hi -= 1
    return max_s
    
if __name__ == "__main__":
    print(twoSumLessThanK_1([34,23,1,24,75,33,54,8],60))
    print(twoSumLessThanK_2([34,23,1,24,75,33,54,8],60))