# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # recursively find max value of left or right tree
        # add 1 when returns the previous max
        if root == None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1 

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """

        # check left tree
        # 
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else: 
                root = root.right
        return succ

 	def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            invert = self.invertTree
            root.left, root.right = invert(root.right), invert(root.left)
            return root

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if (p and q is None) or (p is None and q):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    #   1
    # /   \
    #2     3
    # \
    #  5
    #
    # ["1->2->5", "1->3"]
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        return self.recursive_paths(root, str(root.val), [])
    
    def recursive_paths(self, root, path, paths):
        # no children
        if root.left is None and root.right is None:
            paths.append(path)
        if root.left:
            paths = self.recursive_paths(root.left, path + "->" + str(root.left.val), paths)
        if root.right:
            paths = self.recursive_paths(root.right, path + "->" + str(root.right.val), paths)
        return paths
