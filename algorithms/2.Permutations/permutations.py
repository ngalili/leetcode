# 46. Permutations
# https://leetcode.com/problems/permutations/

import itertools
import copy

def permutation(nums):
    size = len(nums)
    if size == 0:
        return []
    if size == 1:
        return [nums]
    res = []
    for i in range(size):
        remains = nums[:i] + nums[i+1:]
        for val in permutation(remains):
            res.append([nums[i]] + val)
    return res

# using DFS 
def permutation_dfs(nums):
    def dfs(nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
    res = []
    dfs(nums, [], res)
    return res

if __name__ == "__main__":
    nums = [1,2,3]
    for val in itertools.permutations(nums):
        print(val)
    print(permutation(nums))
    print(permutation_dfs(nums))