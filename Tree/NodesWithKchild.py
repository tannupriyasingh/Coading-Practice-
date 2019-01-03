def createTree():
	ht = dict()
	ht["n1"] = (20, ["n2", "n6"])
	ht["n2"] = (30, ["n3", "n4", "n5"])
	ht["n3"] = (40, ["n7"])
	ht["n4"] = (50, [])
	ht["n5"] = (60, [])
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

def nodesWithKchild(k, node, tree):
	if isLeafNode(node, tree):
		if(k == 0):
		   return 1
		return 0
	
	KchildNodes = 0
	childNodes = getNodeChild(node, tree)
	for childNode in childNodes:
		KchildNodes += nodesWithKchild(k, childNode, tree)

	if(len(childNodes) == k):
		KchildNodes += 1

	return KchildNodes

if __name__ == "__main__":
	root, tree = createTree()
	KchildNodes = nodesWithKchild(0, root, tree)
	print("Number of nodes with K child {}".format(KchildNodes))

