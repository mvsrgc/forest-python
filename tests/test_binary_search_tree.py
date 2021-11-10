import pytest
from forest import tree_exceptions
from forest.binary_trees import binary_search_tree


def test_simple_case(basic_tree: list) -> None:
    tree = binary_search_tree.BinarySearchTree()

    assert tree.empty

    for key, data in basic_tree:
        tree.insert(key, data)

    assert tree.empty is False

    with pytest.raises(tree_exceptions.DuplicateKeyError):
        tree.insert(23, "23")

    assert tree.get_leftmost(node=tree.root).key == 1
    assert tree.get_leftmost(node=tree.root).data == "1"
    assert tree.get_rightmost(node=tree.root).key == 34
    assert tree.get_rightmost(node=tree.root).data == "34"
    assert tree.search(key=24).data == "24"
    assert tree.get_height(node=tree.root) == 4
    assert tree.get_predecessor(node=tree.root).key == 22
    temp = tree.search(key=24)
    assert tree.get_predecessor(node=temp).key == 23