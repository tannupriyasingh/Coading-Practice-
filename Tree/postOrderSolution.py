"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

    

class postorderSolution(object):
    
    
    def arrangeNodes(self, node, listOfNodes):
        for childNode in node.children:    
            self.arrangeNodes(childNode, listOfNodes)
        listOfNodes.append(node.val)
        
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        listOfNodes = list()
        
        if root:
            self.arrangeNodes(root, listOfNodes)
        
        
        return listOfNodes