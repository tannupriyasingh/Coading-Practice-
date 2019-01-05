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

def checkBalanced(node, tree):
	if isLeafNode(node, tree):
		balanced = True
		nodeCount = 1;
		return balanced, nodeCount

	S = set()
	for childNode in getNodeChild(node, tree):
		balanced, nodeCount = checkBalanced(childNode, tree)
		S.add(nodeCount)
	
	if(len(S) == 1):
		balanced = True
	else:
		balanced = False
	nodeCount += 1
	return balanced, nodeCount

if __name__ == "__main__":
	root, tree = createTree()

	balanced, nodeCount = checkBalanced(root, tree)
	print("Is Tree Balanced {}".format(balanced))
