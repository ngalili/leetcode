# 112. Path Sum
# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if root == None:
        return False
    if root.left == None and root.right == None: 
        return sum-root.val==0
    return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)