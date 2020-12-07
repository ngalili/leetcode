# 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import List

# traditional way
def nextGreatestLetter(letters: List[str], target: str) -> str:
    target_ord = ord(target)
    last_ord = ord(letters[-1])

    if target_ord >= last_ord:
        return letters[0]

    for index, val in enumerate(letters):
        if ord(val) - target_ord > 0:
            return letters[index]

# because given list is a sorted list, we can use binary search 
def nextGreatestLetter(letters: List[str], target: str) -> str:
    target_ord = ord(target)
    last_ord = ord(letters[-1])

    if target_ord >= last_ord:
        return letters[0]
    
    left, right = 0, len(letters)
    while left < right:
        mid = left + (right - left)//2
        mid_ord = ord(letters[mid])
        if target_ord >= mid_ord:
            left = mid + 1
        else:
            right = mid
    return letters[left]
     
if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "d"
    print(nextGreatestLetter(letters, target))
