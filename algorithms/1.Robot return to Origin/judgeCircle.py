# 657. Robot Return to Origin
# https://leetcode.com/problems/robot-return-to-origin/

import collections

def judgeCircle(moves: str) -> bool:
    startPos = [0,0]
    for move in moves:
        if move == 'U':
            startPos[1] += 1
        elif move == 'D':
            startPos[1] -= 1
        elif move == 'R':
            startPos[0] += 1
        elif move == 'L':
            startPos[0] -= 1
        else:
            continue
    return startPos == [0,0]

def judgeCircle_(moves: str) -> bool:
    c = collections.Counter(moves)
    return c['L'] == c['R'] and c['U'] == c['D']

if __name__ == "__main__":
    print(judgeCircle("LDRRLRUULR"))
    print(judgeCircle_("LDRRLRUULR"))
