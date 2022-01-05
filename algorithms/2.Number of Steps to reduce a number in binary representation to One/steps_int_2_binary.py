# 1404. Number of Steps to Reduce a Number in Binary Representation to One
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

# first solution: convert binary string to integer, then convert it back to binary as the given rules and count the number of steps to reduce
class Solution:
    def numSteps(self, s: str) -> int:
        val = int(s, 2)
        steps = 0
        
        while val > 1:
            if val % 2 == 0:
                val = val // 2
            else:
                val += 1
            steps += 1
        return steps

# second solution: count directly from binary string
# read string from right to left, "1" means that it's an odd number -> we need 2 operators: plus 1 and divide by 2 
class Solution:
    def numSteps(self, s: str) -> int:
        i = len(s) - 1
        steps = 0
        carry = 0

        while i != 0:
            if int(s[i]) + carry == 1: # odd number
                steps += 2
                carry = 1
            else:
                steps += 1
            i -= 1 # [Note: This step is a bit slow (compare with for loop) since it is interpreted. ]

        return steps + carry

# improve the second solution
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1: # odd number
                steps += 2
                carry = 1
            else:
                steps += 1
        
        return steps + carry