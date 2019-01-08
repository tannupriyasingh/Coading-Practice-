# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class inorderTraversalSolution(object):
    
    def inorderArrange(self, node, inorderList):
    
        if node.left == None and node.right == None:
            inorderList.append(node.val)
            return
        if node.left:
            self.inorderArrange(node.left, inorderList)
            
        inorderList.append(node.val)
        
        if node.right:
            self.inorderArrange(node.right, inorderList)
        
        return inorderList   
    
    
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorderList = []
        if root:
            self.inorderArrange(root, inorderList)
        
        return inorderList