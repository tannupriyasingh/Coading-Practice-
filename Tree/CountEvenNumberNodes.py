def createTree():
	ht = dict()
	ht["n1"] = (20, ["n2", "n6"])
	ht["n2"] = (30, ["n3", "n4", "n5"])
	ht["n3"] = (40, ["n7"])
	ht["n4"] = (50, [])
	ht["n5"] = (63, [])
	ht["n6"] = (70, [])
	ht["n7"] = (80, [])
	return "n1" , ht

def isLeafNode(node, tree):
	if len(tree[node][1]) == 0: 
		return True

def getNodeValue(node, tree):
	return tree[node][0]

def getNodeChild(node, tree):
	return tree[node][1]

def countEvenNumberNodes(node, tree):
	if isLeafNode(node, tree):
		if (getNodeValue(node, tree) % 2 == 0):
			return 1
		return 0

	evenNode = 0
	for childNode in getNodeChild(node, tree):
		evenNode += countEvenNumberNodes(childNode, tree)
	
	if(getNodeValue(node, tree) % 2 == 0):
		evenNode += 1
	return evenNode

if __name__ == "__main__":
	root, tree = createTree()
	print("Even number nodes in tree are {}".format(countEvenNumberNodes(root, tree)))
