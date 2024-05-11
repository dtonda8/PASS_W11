from typing import List
from data_structures.array_list import ArrayList
from data_structures.bst import BinarySearchTree

def AL(lst: List) -> ArrayList:
    res = ArrayList(len(lst))
    for num in lst:
        res.append(num)
    return res

def ALtoList(al: ArrayList):
    out = []
    for i in range(len(al)):
        out.append(al[i])
    return out

def matrix_to_AL(mat: List[List[int]]):
    res = ArrayList(len(mat))
    for lst in mat:
        res.append(AL(lst))
    return res

def toBST(arr: List):
    bst = BinarySearchTree()
    for num in arr:
        bst[num] = num
    return bst
    


