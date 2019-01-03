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

def sumOfUniqueNodeValues(node, tree):
	uniqueElements = set()
	if isLeafNode(node, tree):
		uniqueElements.add(getNodeValue(node, tree))
		return uniqueElements

	for childNode in getNodeChild(node, tree):
		uniqueElements = uniqueElements.union(sumOfUniqueNodeValues(childNode, tree))
	
	uniqueElements.add(getNodeValue(node, tree))
	return uniqueElements

if __name__ == "__main__":
	root, tree = createTree()
	uniqueElements = sumOfUniqueNodeValues(root, tree)
	print("Sum of Unique nodes values of tree is {}".format(sum(uniqueElements)))
