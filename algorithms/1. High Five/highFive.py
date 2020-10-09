# 1086. High Five
# https://leetcode.com/problems/high-five/
# Runtime: 60 ms, faster than 99.82% of Python3 online submissions for High Five.
# Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for High Five.

from typing import List
def highFive(items: List[List[int]]) -> List[List[int]]:
    students = {}
    for data in items:
        try:
            students[data[0]].append(data[1])
        except:
            students[data[0]] = [data[1]]

    for i in students:
        students[i].sort(reverse=True)
        students[i] = students[i][:5]

    return [[i,sum(students[i])//len(students[i])] for i in students]

if __name__ == "__main__":
    print(highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
         