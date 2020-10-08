# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/

def reverseInt_1(x):
    if x in range((-1 << 31),(1 << 31)-1):
        tmp = 0
        num = x
        isNegative = False
        if x < 0:
            num = x*(-1)
            isNegative = True
        while num > 0:
            res = num%10
            tmp = tmp*10 + res
            num = num//10
        tmp = isNegative and tmp*(-1) or tmp
        if tmp in range((-1 << 31),(1 << 31)-1):
            return tmp
        else:
            return 0
    else:
        return 0

# optimized algorithm
def reverseInt_2(x):
    num = str(abs(x))
    if x < 0:
        result = -1 * int(num[::-1])
    else:
        result = int(num[::-1])

    if result not in range((-1 << 31), (1 << 31) - 1):
        return 0
    return result

if __name__ == "__main__":
    print(reverseInt_1(-123))
    print(reverseInt_2(-123))