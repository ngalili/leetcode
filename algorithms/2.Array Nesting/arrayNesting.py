# 565. Array Nesting
# https://leetcode.com/problems/array-nesting/

def arrayNesting(nums) -> int:
    visited, res = [0] * len(nums), 0
    for i in nums:
        cnt = 0
        while not visited[i]:
            visited[i] = 1
            cnt += 1
            i = nums[i]
        res = max(res, cnt)
    return res

#improved: referred to other solutions
def arrayNesting_update(nums) -> int:
    res = 0
    for i in range (len(nums)):
        if (nums[i] != -1):
            start = nums[i]
            count = 0
            while (nums[start] != -1):
                temp = start
                start = nums[start]
                count += 1
                nums[temp] = -1
            res = max(res, count)
    return res

if __name__ == "__main__":
    print(arrayNesting([5,4,0,3,1,6,2]))
    print(arrayNesting([0,1,2]))
    print(arrayNesting_update([5,4,0,3,1,6,2]))
    print(arrayNesting_update([0,1,2]))
