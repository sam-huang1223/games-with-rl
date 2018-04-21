"""
REQUIRES SETUP - see README
"""

import os

import pydotplus as pydot
from itertools import zip_longest

from config import GRAPHVIZ_BIN_PATH


class NodeAttributes:  # can be replaced with a dataclass from Python 3.7
    def __init__(self, edge_color):
        self.edge_color = edge_color


class DrawTree:
    def __init__(self, root, children, node_attributes, outputPath):
        self.graph = pydot.Dot(graph_type='digraph')
        self.graph.add_node(pydot.Node(root))
        self.add_edges(root, children, node_attributes)
        self.graph.write_png('{path}_root_{root}.png'.format(path=outputPath, root=root))

    def add_edges(self, parent, children, node_attributes):
        for child, attributes in zip_longest(children, node_attributes):
            if isinstance(child, tuple):
                color = attributes[0].edge_color if isinstance(attributes, tuple) else 'black'
                self.graph.add_edge(pydot.Edge(parent, child[0], color=color))
                self.add_edges(child[0], child[1:],
                               attributes[1:] if attributes else ())  # first item of tuple is root of subtree
            else:
                color = attributes.edge_color if attributes else 'black'
                self.graph.add_edge(pydot.Edge(parent, child, color=color))


def draw_trees(trees, node_attributes=(), outputPath='tree'):
    os.environ["PATH"] += os.pathsep + GRAPHVIZ_BIN_PATH

    for num, tree in enumerate(trees.keys()):
        DrawTree(tree, trees[tree], node_attributes, outputPath)
