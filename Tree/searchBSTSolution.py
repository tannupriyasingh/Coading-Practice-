# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class searchBSTSolution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return []
        
        if root.val == val:
            return root
             
        else:
            if(root.val>val):
                return self.searchBST(root.left, val)
            return self.searchBST(root.right, val)
    