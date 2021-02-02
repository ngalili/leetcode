# 136. Single Number
# https://leetcode.com/problems/single-number/

from typing import List
# normal way
def singleNumber_0(nums: List[int]) -> int:
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
        else:
            unique_nums.remove(num)
    return unique_nums[0]

# using hash table
def singleNumber_1(nums: List[int]) -> int:
    hashtbl = {}
    for num in nums:
        try:
            hashtbl.pop(num)
        except:
            hashtbl[num] = 1
    return hashtbl.popitem()[0]

# using bit manipulation
def singleNumber_2(nums: List[int]) -> int:
    a = 0
    for num in nums:
        a ^= num
    return a

# using math - Time complexity: O(2*N) = O(N)
def singleNumber_3(nums: List[int]) -> int:
    return 2*sum(set(nums)) - sum(nums)

if __name__ == "__main__":
    testdata = [1,2,3,2,1,4,5,3,5]
    print(singleNumber_0(testdata))
    print(singleNumber_1(testdata))
    print(singleNumber_2(testdata))
    print(singleNumber_3(testdata))
