import dataclasses
from typing import Any, Optional

from forest import tree_exceptions


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

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, key: Any) -> None:
        pass

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
