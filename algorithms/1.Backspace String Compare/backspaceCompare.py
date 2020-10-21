# 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/

def removeSpace(Str: str) -> str:
    if "#" in Str:
        i = 0
        while i < len(Str):
            if Str[i] == "#":
                if i == 0:
                    Str = Str[1:]
                    i = 0
                    continue
                else:
                    Str = Str[:i-1] + Str[i+1:]
                    i = 0 
                    continue
            i += 1
    return Str
    
def backspaceCompare(S: str, T: str) -> bool:
    return removeSpace(S) == removeSpace(T)

# using stack 
def backspaceCompare_(S: str, T: str) -> bool:
    def removeSpace(Str: str) -> str:
        stack = []
        for val in Str:
            if val == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(val)
        return stack
        
    return removeSpace(S) == removeSpace(T)

if __name__ == "__main__":
    print(backspaceCompare("ab#c","ad#c"))
    print(backspaceCompare_("ab##","c#d#"))