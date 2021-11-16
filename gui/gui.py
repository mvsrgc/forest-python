from typing import Any, Iterator
import dearpygui.dearpygui as dpg

from forest.binary_trees import binary_search_tree
from forest.binary_trees import traversal

i = 0

def create_tree():
    binary_tree = binary_search_tree.BinarySearchTree()

    nodes = [
        (23, "23"),
        (4, "4"),
        (30, "30"),
        (11, "11"),
        (7, "7"),
        (34, "34"),
        (20, "20"),
        (24, "24"),
        (22, "22"),
        (15, "15"),
        (1, "1"),
        (2, "2"),
    ]

    for key, data in nodes:
        binary_tree.insert(key=key, data=data)

    return binary_tree


def knuth_layout(node: binary_search_tree.Node, depth: int):
    global i
    if node.left:
        knuth_layout(node.left, depth + 50)
    i += 50
    node.x = i
    node.y = depth
    if node.right:
        knuth_layout(node.right, depth + 50)


def create_window(nodes: list[tuple[Any, Any, Any, Any]]):
    dpg.create_context()

    dpg.create_viewport(title="Custom Title", x_pos=0, y_pos=0, width=1200, height=800)

    with dpg.window(label="Settings", width=400, height=800):
        dpg.add_text("Tree")
        dpg.add_slider_int(
            label="Number of nodes", min_value=1, max_value=10, default_value=5
        )
        dpg.add_slider_int(
            label="Max. node value", min_value=10, max_value=100, default_value=10
        )
        dpg.add_spacer(height=10)
        dpg.add_button(label="Apply")
        dpg.add_spacer(height=10)
        dpg.add_separator()
        dpg.add_text("Nodes In Tree (Inorder traversal)")
        dpg.add_text(",".join(str(item[0]) for item in tree_nodes))

    with dpg.window(label="Visualization", width=800, height=800, pos=(400, 0)):
        for item in nodes:
            dpg.draw_circle((item[2] + 50, item[3] + 50), 25)
            dpg.draw_text((item[2] + 50 - 5, item[3] + 50 - 5), item[0], size=15)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    tree = create_tree()
    knuth_layout(tree.root, 1)
    tree_nodes = list(traversal.inorder_traverse(tree))
    create_window(tree_nodes)
