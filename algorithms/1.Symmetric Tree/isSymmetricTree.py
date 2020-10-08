# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def insert(self, val):
        # Compare the new value with the parent node
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

def isMirror(node1: TreeNode, node2: TreeNode)->bool:
    if node1 is None and node2 is None: # symmetric if the tree is empty 
        return True
    elif node1 is None or node2 is None:
        return False
    
    return (node1.val == node2.val and
        isMirror(node1.left, node2.right) and 
        isMirror(node1.right, node2.left))
    
def isSymmetric(root: TreeNode) -> bool:
    return isMirror(root,root)

if __name__ == "__main__":
    # [1,2,2,3,4,4,3]
    test = TreeNode(1)
    test.insert(2)
    test.insert(2)
    test.insert(3)
    test.insert(4)
    test.insert(4)
    test.insert(3)
    print(isSymmetric(test))

    # [1,2,2,null,3,null,3]
    test_ = TreeNode(1)
    test_.insert(2)
    test_.insert(2)
    test_.insert(None)
    test_.insert(3)
    test_.insert(None)
    test_.insert(3)
    
    print(isSymmetric(test_))