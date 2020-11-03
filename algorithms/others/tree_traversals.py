# Binary Tree 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
    
# Depth First Traversal: Inorder
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val)
        print_inorder(root.right)

# Depth First Traversal: Preorder
def print_preorder(root):
    if root:
        print(root.val)
        print_preorder(root.left)
        print_preorder(root.right)

# Depth First Traversal: Postorder
def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val)

# Breadth First Traversal
def print_bfs(root):
    def height(node):
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            l_height = height(node.left)
            r_height = height(node.right)

            # return the larger one
            return l_height + 1 if l_height > r_height else r_height + 1
            
    # Function to print level order traversal of tree
    def print_lvl_order(root):
        h = height(root)
        for i in range(1, h + 1):
            print_given_lvl(root, i)
    
    def print_given_lvl(root, level):
        if root is None:
            return
        if level == 1:
            print(root.val, end =" ")
        elif level > 1:
            print_given_lvl(root.left, level - 1)
            print_given_lvl(root.right, level - 1)
    
    print_lvl_order(root)

# Breadth First Traversal - using queue
def print_bfs_using_queue(root):
    if root is None:
        return
    queue = []
    queue.append(root)

    while len(queue) > 0:
        # Print front of queue and remove it from queue
        print(queue[0].val)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)
        
        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

if __name__ == "__main__":
    # Driver code 
    root = Node(1) 
    root.left      = Node(2) 
    root.right     = Node(3) 
    root.left.left  = Node(4) 
    root.left.right  = Node(5)
    
    print("Inorder traversal of binary tree is \n")
    print_inorder(root)

    print("Preorder traversal of binary tree is \n")
    print_preorder(root)

    print("Postorder traversal of binary tree is \n")
    print_postorder(root)

    print("Breadth First traversal of binary tree is \n")
    print_bfs(root)

    print("Breadth First traversal of binary tree (using queue) is \n")
    print_bfs_using_queue(root)

    
