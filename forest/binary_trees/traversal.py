from typing import Any, Iterator

from forest.binary_trees import binary_search_tree as BinarySearchTree

Pairs = Iterator[tuple[Any, Any, Any, Any]]


def inorder_traverse(tree: BinarySearchTree) -> Pairs:
    nodes_numbered = 0
    return _inorder_traverse(tree.root)


def _inorder_traverse(node: BinarySearchTree.Node) -> Pairs:
    if node:
        yield from _inorder_traverse(node.left)
        yield (node.key, node.data, node.x, node.y)
        yield from _inorder_traverse(node.right)
