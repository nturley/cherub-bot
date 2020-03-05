from trees.tree import build_tree
import py_trees

tree_path = 'tree.json'
tree = build_tree(tree_path, None)
print(py_trees.display.ascii_tree(tree.root))