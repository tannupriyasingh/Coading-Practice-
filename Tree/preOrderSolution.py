"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    
    def arrangeNodes(self, node, listOfNodes):
        listOfNodes.append(node.val) 
        for childNodes in node.children:
            self.arrangeNodes(childNodes, listOfNodes)
        
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        listOfNodes = []
        
        if root:
            self.arrangeNodes(root, listOfNodes)
        
        return listOfNodes
                  