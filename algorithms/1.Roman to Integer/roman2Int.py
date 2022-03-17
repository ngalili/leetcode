# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
  
def romanToInt(str): 
    value = { 
        'M': 1000, 
        'D': 500, 
        'C': 100, 
        'L': 50, 
        'X': 10, 
        'V': 5, 
        'I': 1
    }
    res = 0
    i = 0
    
    while i < len(str):
        s1 = value[str[i]] 
        if i < len(str) - 1:
            s2 = value[str[i + 1]]
            if s1 >= s2:
                res += s1
                i += 1
            else:
                res = res - s1 + s2
                i += 2
        else:
            res += s1
            i += 1
    return res 

# Improved algorithm - referred to Leetcode's Solution
def romanToInt_update(s): 
    value = { 
        'M': 1000, 
        'D': 500, 
        'C': 100, 
        'L': 50, 
        'X': 10, 
        'V': 5, 
        'I': 1
    }
    res = value[s[-1]]
    for i in reversed(range(len(s) - 1)):
        if value[s[i]] < value[s[i+1]]:
            res -= value[s[i]]
        else:
            res += value[s[i]]
    return res

# 2022/03/17 - re-do this problem
def romanToInt(self, s: str) -> int:
    myRoman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    res = 0
    for index in range(len(s)):
        if index < len(s) - 1:
            if myRoman[s[index]] < myRoman[s[index + 1]]:
                res = res - myRoman[s[index]]
            else: 
                res = res + myRoman[s[index]]
        else:
            res = res + myRoman[s[index]]
    return res
  
if __name__ == "__main__":
    print(romanToInt("MCMXCIV"))
    print(romanToInt_update("MCMXCIV"))
