"""
BREAKS

REQUIRES SETUP - see README

Given the root of a graph, the object that represents a node in the graph, and the output file path, this
algorithm can recursively visualize the nodes and connection in any graph

Created for visualizing trees (e.g. move histories) - not good for densely connected graphs
*This program was developed to maximize user control in creating a graph visualization

Notes to help you understand test_graph_viz.png:
    Any node with value of root_id-# are placeholder nodes that represent empty neighboring nodes (based on node.neighbors)
    Nodes with a value of # are nodes that have been assigned a real value
    Node values are their id numbers, assigned at their creation

Next steps:
1) Allow for customization of node/edge features (e.g. fill color)
2) Test if this algorithm works with no neighbors (i.e. empty ~ [])
"""

### Made redundant by bokeh board visualization - need to find alternative use for this code
### (perhaps visualizing move history?)

import os

import pydotplus as pydot

from config import GRAPHVIZ_BIN_PATH


class NodeAttributes:  # can be replaced with a dataclass from Python 3.7
    def __init__(self, node_color=None, edge_color=None):
        self.node_color = node_color
        self.edge_color = edge_color


class DrawGraph:
    def __init__(self, root, node_obj_representation, output_path):
        graph_representation = convert_to_graph_representation(root, node_obj_representation)
        visualizer_input = [graph_representation[0], graph_representation[1:]]
        # input format for visualizer: [root, children] ~ [root, [[root (child 1), child 1 child 1], child 2,...]]

        self.graph = pydot.Dot(graph_type='digraph')
        self.graph.add_node(pydot.Node(visualizer_input[0], ))
        self.add_edges(visualizer_input[0], visualizer_input[1])
        self.graph.write_png(output_path)

    def add_edges(self, parent, children):
        for child in children:
            if isinstance(child, list):
                self.graph.add_edge(pydot.Edge(parent, child[0]))
                self.add_edges(child[0], child[1:])  # first item of tuple is root of subtree
            else:
                self.graph.add_edge(pydot.Edge(parent, child))


def convert_to_graph_representation(root, node_obj_representation):
    output = [root.id]

    for child in root.neighbors:
        if isinstance(child, node_obj_representation):
            break
    else:  # if loop was never broken (i.e. if no Node objects in list of children)
        for child_num in range(1, len(root.neighbors) + 1):
            output.append("{root}-{child_num}".format(root=root.id, child_num=child_num))
        return output

    for child_num, child in enumerate(root.neighbors):
        if child:
            output.append(convert_to_graph_representation(child, node_obj_representation))
        else:
            output.append("{root}-{child_num}".format(root=root.id, child_num=child_num))
    return output


def draw_graph(root, node_obj_representation, output_path=''):
    os.environ["PATH"] += os.pathsep + GRAPHVIZ_BIN_PATH

    DrawGraph(root, node_obj_representation, output_path)
