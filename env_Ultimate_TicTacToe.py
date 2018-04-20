from visualize_graph import draw_trees


class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.neighbors = []  # allows for 8 neighbors

        assert len(self.neighbors) <= 8, "More than 8 neighbors for node {}".format(self.id)


def id_generator():
    for i in range(1, 81+1):  # 9*9 possible positions
        yield i


class UltimateTTT:
    def __init__(self):
        ids = id_generator()

        a = Node(next(ids), 1)
        print(a.id)
        b = Node(next(ids), 1)
        print(b.id)

    def create_nodes(self):
        raise NotImplementedError

    def step(self, node_id):
        self.check_win()
        raise NotImplementedError

    def check_win(self):
        raise NotImplementedError

    def draw_graph(self):
        draw_trees(self._get_graph())

    def _get_graph(self):
        raise NotImplementedError


game = UltimateTTT()

