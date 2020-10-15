# 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    res = 0
    if root is None:
        return 0
    if L <= root.val <= R:
        res += root.val
    if root.left:
        res += self.rangeSumBST(root.left, L, R)
    if root.right:
        res += self.rangeSumBST(root.right, L, R)
    return res

# improved algorithm - referred to Leetcode's solution. 
def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    res = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if L <= node.val <= R:
                res += node.val
            if L < node.val:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
    return res
                
