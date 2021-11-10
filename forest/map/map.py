from typing import Any, Optional

from forest.binary_trees import binary_search_tree


class Map:
    def __init__(self):
        self._bst = binary_search_tree.BinarySearchTree()

    def __setitem__(self, key: Any, value: Any) -> None:
        self._bst.insert(key, value)

    def __getitem__(self, key: Any) -> Optional[Any]:
        node = self._bst.search(key)
        if node:
            return node.data
        return None

    def __delitem__(self, key: Any) -> None:
        self._bst.delete(key)

    @property
    def empty(self) -> bool:
        return self._bst.empty


if __name__ == "__main__":
    contacts = Map()

    contacts["joe"] = "joe@joe.com"
    contacts["bob"] = "bob@bob.com"
    contacts["jane"] = "jane@jane.com"

    assert contacts["jane"] == "jane@jane.com"

    del contacts["jane"]

    assert contacts["jane"] is None

    print(contacts["joe"])
