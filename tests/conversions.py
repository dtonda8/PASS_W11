from typing import List
from data_structures.bst import BinarySearchTree

def toBST(arr: List):
    bst = BinarySearchTree()
    for num in arr:
        bst[num] = num
    return bst
    


