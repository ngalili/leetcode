# 559. Maximum Depth of N-ary Tree
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    # Using DFS 
    # Note: DFS is commonly used when you need to search the entrie tree.
    # It's easier to implement (using recursion) than BFS, and requires less state. 
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            heights = [maxDepth(c) for c in root.children]
        return max(heights) + 1
    # same resolution but this's shorter
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        return 1 + max(map(self.maxDepth, root.children or [None]))
    
    # using DFS (use a stack)
    def maxDepth(self, root: 'Node') -> int:
        stack = []
        depth = 0
        if root: stack.append((root, 1))
        while stack:
            (node, d) = stack.pop()
            depth = max(depth, d)
            for child in node.children:
                stack.append((child, d+1))
        return depth

    # using BFS (use a queue)
    def maxDepth(self, root: 'Node') -> int:
        queue = []
        depth = 0
        if root: queue.append((root, 1))
        for (node, level) in queue:
            depth = level
            queue += [(child, level + 1) for child in node.children]
        return depth