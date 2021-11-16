from typing import Any
import dearpygui.dearpygui as dpg

from forest.binary_trees import binary_search_tree
from forest.binary_trees import traversal


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
    ]

    for key, data in nodes:
        binary_tree.insert(key=key, data=data)

    return binary_tree


def create_window(tree_nodes: list[tuple[Any, Any]]):
    dpg.create_context()

    dpg.create_viewport(title="Custom Title", x_pos=0, y_pos=0, width=1200, height=800)
    dpg.set_viewport_max_height(800)
    dpg.set_viewport_max_width(1200)

    xdata = [index for index, item in enumerate(tree_nodes)]
    ydata = [item[0] for item in tree_nodes]

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
        dpg.add_text(
            ",".join(str(item[0]) for item in tree_nodes)
        )

    with dpg.window(label="Visualization", width=800, height=800, pos=(400, 0)):
        pass

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    tree = create_tree()
    tree_nodes = list(traversal.inorder_traverse(tree))
    create_window(tree_nodes)
