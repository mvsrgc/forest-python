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

    assert tree.search(24).data == "24"
