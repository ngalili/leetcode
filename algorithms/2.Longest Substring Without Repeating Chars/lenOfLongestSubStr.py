# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def lengthOfLongestSubstring(s: str) -> int:
    res = []
    max_len = 0
    for c in s:
        if c in res:
            res = res[res.index(c)+1:]
        res.append(c)
        max_len = max(max_len, len(res))
    return max_len

# improved 
def lengthOfLongestSubstring(s: str) -> int:
    max_len = start = 0
    res = {}
    for i, c in enumerate(s):
        if c in res and start <= res[c]:
            start = res[c] + 1
        else:
            max_len = max(max_len, i - start + 1)
        res[c] = i
    return max_len
   
if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("pwwkew"))
