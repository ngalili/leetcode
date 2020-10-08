# 1133. Largest Unique Number
# https://leetcode.com/problems/largest-unique-number/

def isLargestUniqueNumber(lst):
    tmp = {}
    for val in lst:
        try:
            tmp[val] += 1
        except:
            tmp[val] = 1
    maxVal = -1
    for index, value in tmp.items():
        if value == 1:
            maxVal = max(maxVal, index)
    return maxVal

if __name__ == "__main__":
    test = [5,7,3,9,4,9,8,3,1]
    print(isLargestUniqueNumber(test))
