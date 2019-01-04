def createTree():
	ht = dict()
	ht["n1"] = (20, ["n2", "n6"])
	ht["n2"] = (30, ["n3", "n4", "n5"])
	ht["n3"] = (40, [])
	ht["n4"] = (50, [])
	ht["n5"] = (60, [])
	ht["n6"] = (70, [])
	#ht["n7"] = (80, [])
	return "n1" , ht

def isLeafNode(node, tree):
	if len(tree[node][1]) == 0: 
		return True

def getNodeValue(node, tree):
	return tree[node][0]

def getNodeChild(node, tree):
	return tree[node][1]

def heightOfTree(node, tree):
	if isLeafNode(node, tree):
		return 1

	height = 0
	for childNode in getNodeChild(node, tree):
		height=max(heightOfTree(childNode, tree), height)
	
	height += 1
	return height

def sameSkeletonSubTree(rangeHeight, node, tree):
	curHeight = rangeHeight[0]
	res = [0]*rangeHeight[1]
	isSkeleton = True

	if isLeafNode(node, tree):
		res[curHeight] = 1
		isSkeleton = True
		return res, isSkeleton
	
	flag = True
	childRangeHeight = (curHeight+1, rangeHeight[1])
	for childNode in getNodeChild(node, tree):
		temp, tempSkeleton = sameSkeletonSubTree(childRangeHeight, childNode, tree)
		if flag:
			checkSiblingSkeleton = temp
			flag = False
		
		if (checkSiblingSkeleton == temp) and isSkeleton:
			isSkeleton = True
		else:
			isSkeleton = False
		res = [res[i] + temp[i] for i in range(len(temp))]
	
	res[curHeight] = 1	
	return res, isSkeleton

if __name__ == "__main__":
	root, tree = createTree()
	height = heightOfTree(root, tree)
	nodeCountArr, isSkeleton = sameSkeletonSubTree((0, height), root, tree)
	print("Tree has same skeleton subtree : {}".format(isSkeleton))
