# 137. Single Number II
# https://leetcode.com/problems/single-number-ii/

from typing import List
# normal way
def singleNumber_0(nums: List[int]) -> int:
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in dic:
        if dic[i] == 1:
            return i

# using bitwise
def singleNumber_1(nums: List[int]) -> int:
    def convert(x):
        if x >= 2**31:
            x -= 2**32
        return x

    ans = 0
    for i in range(0, 32):
        count = 0
        for num in nums:
            if ((num >> i) & 1):
                count += 1
        ans |= ((count%3) << i)
    return convert(ans)

# using bit manipulation
def singleNumber_2(nums: List[int]) -> int:
    low_bits, high_bits = 0, 0
    for num in nums:
        low_bits = ~high_bits&(low_bits^num)
        high_bits = ~low_bits&(high_bits^num)
    return low_bits

# using math
def singleNumber_3(nums: List[int]) -> int:
    return (3*sum(set(nums)) - sum(nums))//2

if __name__ == "__main__":
    testdata = [1,2,3,2,1,4,5,3,5,2,1,3,5]
    print(singleNumber_1(testdata))
    print(singleNumber_2(testdata))
    print(singleNumber_3(testdata))
