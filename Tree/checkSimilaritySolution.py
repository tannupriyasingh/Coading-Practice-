# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class checkSimilaritySolution(object):
    
    def checkSimilarity(self, treeList, node):
        if node:
            if (node.left is None and node.right is None):
                treeList.append(node.val)
                return treeList
            else:
                treeList = self.checkSimilarity(treeList, node.left)
                treeList = self.checkSimilarity(treeList, node.right)
        
        return treeList
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        tree1 = list()
        tree2 = list()
        if root1 or root2:
            tree1 = self.checkSimilarity(tree1, root1)
            tree2 = self.checkSimilarity(tree2, root2)
            
        return tree1 == tree2