from data_structures.bst import BinarySearchTree
from tests.conversions import toBST

def getMinimumDifference(bst: BinarySearchTree) -> int:
	ans = 10 ** 5 + 1 ## or float("inf") 
	it = iter(bst)
	prev_node = next(it)
	for node in it:
		diff = node.key - prev_node.key
		ans = min(ans, diff) ##
		prev_node = node
	return ans ## 

if __name__ == "__main__":
	getMinimumDifference(toBST([4,2,6,1,3]))