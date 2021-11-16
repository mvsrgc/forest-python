from forest.binary_trees import binary_search_tree as BinarySearchTree

from forest.binary_trees import traversal


def test_binary_search_tree_traversal(basic_tree):
    tree = BinarySearchTree.BinarySearchTree()

    for key, data in basic_tree:
        tree.insert(key=key, data=data)

    assert [item for item in traversal.inorder_traverse(tree)] == [
        (1, "1"),
        (4, "4"),
        (7, "7"),
        (11, "11"),
        (15, "15"),
        (20, "20"),
        (22, "22"),
        (23, "23"),
        (24, "24"),
        (30, "30"),
        (34, "34"),
    ]
