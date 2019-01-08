# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionisUnivalTree(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s = set()
        def findUnival(node):
            if node:
                s.add(node.val)
                findUnival(node.left)
                findUnival(node.right)
                
        findUnival(root)
            
        return (len(s) == 1)
            