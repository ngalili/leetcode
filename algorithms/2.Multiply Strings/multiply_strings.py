# 43. Multiply Strings
# https://leetcode.com/problems/multiply-strings/
# Note: must not use any built-in BigInteger lib or convert the inputs to integer directly

def multiply(num1: str, num2: str) -> str:
    res = [0]*(len(num1) + len(num2))
    pos = len(res) - 1

    for n1 in reversed(num1):
        tmp_pos = pos
        for n2 in reversed(num2):
            int1 = ord(n1) - ord('0')
            int2 = ord(n2) - ord('0')
            res[tmp_pos] += int1*int2
            res[tmp_pos - 1] += res[tmp_pos]//10
            res[tmp_pos] %= 10
            tmp_pos -= 1
        pos -= 1
    pointer = 0
    while pointer < len(res) - 1 and res[pointer] == 0:
        pointer += 1 
    
    return ''.join(map(str, res[pointer:]))
         
if __name__ == "__main__":
    print(multiply("2", "3"))
    print(multiply("0", "0"))
    print(multiply("123", "864"))