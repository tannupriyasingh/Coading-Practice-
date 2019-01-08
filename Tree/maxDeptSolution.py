"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class maxDeptSolution(object):
    
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        height = 0
        if root:
            if root.children == []:
                return 1
        
            for childNode in root.children:
                height = max(height, self.maxDepth(childNode))
        
            height += 1
        
        return height