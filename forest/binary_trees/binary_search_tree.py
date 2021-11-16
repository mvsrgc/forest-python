import dataclasses
from typing import Any, Optional, Iterator

from forest import tree_exceptions

Pairs = Iterator[tuple[Any, Any]]


@dataclasses.dataclass
class Node:
    key: Any
    data: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    parent: Optional["Node"] = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def search(self, key: Any) -> Optional[Node]:
        current_node: Optional[Node] = self.root

        while current_node:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return current_node

        return None

    def insert(self, key: Any, data: Any) -> None:
        new_node = Node(key=key, data=data)
        parent: Optional[Node] = None
        current_node: Optional[Node] = self.root

        while current_node:
            parent = current_node
            if new_node.key < current_node.key:
                current_node = current_node.left
            elif new_node.key > current_node.key:
                current_node = current_node.right
            else:
                raise tree_exceptions.DuplicateKeyError(key=key)

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, key: Any) -> None:
        deleting_node = self.search(key=key)

        if self.root is None or deleting_node is None:
            return None

        if deleting_node.left is None:
            self._transplant(
                deleting_node=deleting_node, replacing_node=deleting_node.right
            )
        elif deleting_node.right is None:
            self._transplant(
                deleting_node=deleting_node, replacing_node=deleting_node.left
            )
        else:
            replacing_node = BinarySearchTree.get_leftmost(node=deleting_node.right)
            # The leftmost node is not the direct child of the deleting node
            if replacing_node.parent != deleting_node:
                self._transplant(
                    deleting_node=replacing_node,
                    replacing_node=replacing_node.right,
                )
                replacing_node.right = deleting_node.right
                replacing_node.right.parent = replacing_node
            self._transplant(deleting_node=deleting_node, replacing_node=replacing_node)
            replacing_node.left = deleting_node.left
            replacing_node.left.parent = replacing_node

    def _transplant(self, deleting_node: Node, replacing_node: Optional[Node]) -> None:
        if deleting_node.parent is None:
            self.root = replacing_node
        elif deleting_node == deleting_node.parent.left:
            deleting_node.parent.left = replacing_node
        else:
            deleting_node.parent.right = replacing_node

        if replacing_node:
            replacing_node.parent = deleting_node.parent

    @property
    def empty(self) -> bool:
        return self.root is None

    @staticmethod
    def get_leftmost(node: Node) -> Node:
        current_node = node
        while current_node.left:
            current_node = current_node.left

        return current_node

    @staticmethod
    def get_rightmost(node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    @staticmethod
    def get_height(node: Node) -> int:
        if node.left and node.right:
            return (
                max(
                    BinarySearchTree.get_height(node=node.left),
                    BinarySearchTree.get_height(node=node.right),
                )
                + 1
            )

        if node.left:
            return BinarySearchTree.get_height(node=node.left) + 1

        if node.right:
            return BinarySearchTree.get_height(node=node.right) + 1

        return 0

    @staticmethod
    def get_predecessor(node: Node) -> Optional[Node]:
        if node.left:  # Case 1: left child is not empty
            return BinarySearchTree.get_rightmost(node=node.left)
        # Case 2: left child is empty
        parent = node.parent
        while parent and (node == parent.left):
            node = parent
            parent = parent.parent
        return parent

    @staticmethod
    def get_successor(node: Node) -> Optional[Node]:
        if node.right:
            return BinarySearchTree.get_leftmost(node=node.right)
        parent = node.parent

        while parent and (node == parent.right):
            node = parent
            parent = parent.parent

        return parent
