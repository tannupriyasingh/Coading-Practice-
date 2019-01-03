def createTree():
	ht = dict()
	ht["n1"] = (20, ["n2", "n6"])
	ht["n2"] = (30, ["n3", "n4", "n5"])
	ht["n3"] = (40, [])
	ht["n4"] = (50, [])
	ht["n5"] = (60, [])
	ht["n6"] = (70, [])
	return "n1" , ht

def isLeafNode(node, tree):
	if len(tree[node][1]) == 0: 
		return True

def getNodeValue(node, tree):
	return tree[node][0]

def getNodeChild(node, tree):
	return tree[node][1]

def printLeafNodesTree(root, tree):
	if isLeafNode(root, tree):
		nodeValue = getNodeValue(root, tree)
		print("node id: {}, node value: {}".format(root, nodeValue))
		return 

	for childNode in getNodeChild(root, tree):
		printLeafNodesTree(childNode, tree)
	

def sumOfNodes(node, tree):
	if isLeafNode(node, tree):
		return getNodeValue(node, tree)

	finalSum = 0
	for childNode in getNodeChild(node, tree):
		finalSum += sumOfNodes(childNode, tree)
	
	finalSum += getNodeValue(node, tree)
	
	return finalSum

if __name__ == "__main__":
	root, tree = createTree()
	print(tree)


	printLeafNodesTree(root, tree)

	sumOfTree = sumOfNodes(root, tree)
	print("Sum of the nodes of tree is {}".format(sumOfTree))
