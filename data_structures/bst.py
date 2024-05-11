""" Binary Search Tree ADT.
    Defines a Binary Search Tree with linked nodes.
    Each node contains a key and item as well as references to the children.
"""

from __future__ import annotations

__author__ = 'Brendon Taylor, modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from typing import TypeVar, Generic
from data_structures.node import TreeNode


# generic types
K = TypeVar('K')
I = TypeVar('I')


class BinarySearchTree(Generic[K, I]):
    """ Basic binary search tree. """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        self.root = None

    def __setitem__(self, key: K, item: I) -> None:
        """ Magic method invoking insert_aux(). """
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: TreeNode, key: K, item: I) -> TreeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
            :raise: KeyError if the key already exists
            :complexity best: O(CompK) inserts the item at the root.
            :complexity worst: O(CompK * D) inserting at the bottom of the tree
            where D is the depth of the tree
            CompK is the complexity of comparing the keys
        """
        if current is None:  # base case: at the leaf
            current = TreeNode(key, item)
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            raise KeyError('Inserting duplicate item')
        return current

    def inorder(self, f: Callable) -> None:
        """
        Preforms a in-order traversal of the tree
        :complexity: O(N) where N is number of nodes in the tree
        """
        self.inorder_aux(self.root, f)

    def inorder_aux(self, current: T, f: Callable) -> None:
        """
        Actual in-order traversal of the tree
        :complexity: O(N) where N is number of nodes in the tree
        """
        if current is not None:  # if not a base case
            self.inorder_aux(current.left, f)
            f(current.item)
            self.inorder_aux(current.right, f)