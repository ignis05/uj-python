class GraphEdge:
    node1 = None
    node2 = None
    data = dict(value=0, intree=False)

    def __init__(self, node1, node2, value):
        self.node1 = node1
        self.node2 = node2
        self.data['value'] = value

    def getOtherNode(self, node):
        if self.node1 == node:
            return self.node2
        else:
            return self.node1


class GraphNode:
    data = dict(x=0, y=0, inTree=False)
    edges: list[GraphEdge] = []

    @property
    def getNeighbors(self):
        return [edge.getOtherNode(self) for edge in self.edges]


class Graph:
    nodes = []

    def connect(node1: GraphNode, node2: GraphNode, value: int = 1):
        edge = GraphEdge(node1, node2, value)
        node1.edges.append(edge)
        node2.edges.append(edge)
