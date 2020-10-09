# 1480. Running Sum of 1d Array
# https://leetcode.com/

from typing import List
def runningSum(nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
        if i == 0:
            res.append(nums[i])
        else:
            res.append(res[i-1] + nums[i])
    return res

if __name__ == "__main__":
    print(runningSum([3,1,2,10,1]))