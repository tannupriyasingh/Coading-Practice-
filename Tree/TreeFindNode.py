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

def findNode(numReq, node, tree):
	nodeValue = getNodeValue(node, tree)
	
	if isLeafNode(node, tree):
		if(nodeValue == numReq):
			return True
		return False

	for childNode in getNodeChild(node, tree):
		if findNode(numReq, childNode, tree):
			return True
	
	if nodeValue == numReq:
		return True;	
	
	return False

if __name__ == "__main__":
	root, tree = createTree()
	numFound = findNode(50, root, tree)
	print("Number is avalable in tree {}".format(numFound))
