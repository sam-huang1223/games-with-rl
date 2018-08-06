import pydotplus as pydot  # http://pydotplus.readthedocs.io/reference.html

import os

from config import GRAPHVIZ_BIN_PATH

class Tree:
    def __init__(self, root):
        os.environ["PATH"] += os.pathsep + GRAPHVIZ_BIN_PATH  # allow for usage oh graphviz

        self.tree = pydot.Dot(graph_type='digraph')
        self.root = root
        self.tree.add_node(pydot.Node(self.root.value))
        self.tree.add_edge(pydot.Edge(self.root.value, self.root.children[0].value))
        self.tree.add_edge(pydot.Edge(self.root.value, self.root.children[1].value))

        self.tree.write_png('output/test.png')