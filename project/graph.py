from queue import PriorityQueue
from random import randint


class GraphEdge:
    def __init__(self, node1, node2, weight: int):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        self.inTree = False

    def getOtherNode(self, node):
        "Takes one of this edge's node as an argument and returns the other node"
        if self.node1 == node:
            return self.node2
        else:
            return self.node1

    # comparison operators for priorityqueue
    def __gt__(self, other):
        return self.weight > other.weight

    def __gt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f'Edge({self.node1.i}=={self.node2.i})'


class GraphNode:
    def __init__(self, x: int, y: int, i: int):
        self.x = x
        self.y = y
        self.i = i
        self.edges: list[GraphEdge] = []
        self.inTree = False

    @property
    def getNeighbors(self):
        "Returns a list of all Nodes that are neighbours of this node"
        return [edge.getOtherNode(self) for edge in self.edges]

    def __str__(self):
        return f'Node({self.i})'


class Graph:
    def __init__(self):
        self.nodes: list[GraphNode] = []

    def addNode(self, x: int, y: int):
        "Creates a new node with given x,y coordinates"
        node = GraphNode(x, y, len(self.nodes))
        self.nodes.append(node)
        return node

    def connect(self, node1: GraphNode, node2: GraphNode, weight: int = 1):
        "Connects two nodes with an edge of given weight"
        for edge in node1.edges:
            if edge.getOtherNode(node1) == node2:
                return

        edge = GraphEdge(node1, node2, weight)
        node1.edges.append(edge)
        node2.edges.append(edge)

    def find(self, x, y):
        "Finds and returns a node based on its coordinates"
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node

    def areCoordsConnected(self, x1, y1, x2, y2):
        "Checks if nodes at given coordinates are connected within the created spanning tree"
        node1 = self.find(x1, y1)
        node2 = self.find(x2, y2)
        for edge in node1.edges:
            if not edge.inTree:
                continue
            if edge.getOtherNode(node1) == node2:
                return True
        return False

    def connectByCoords(self, x1, y1, x2, y2):
        "Creates connection with random weight between two nodes of given coordinates"
        self.connect(
            self.find(x1, y1),
            self.find(x2, y2),
            randint(0, 999999999))

    def createGrid(self, width: int, height: int):
        "creates nodes in a grid, where each node is connected to up to 4 neighbours"
        self.nodes = []
        for y in range(height):
            for x in range(width):
                self.addNode(x, y)

        for y in range(height):
            for x in range(width):
                if x > 0:
                    self.connectByCoords(x, y, x-1, y)
                if x < width - 1:
                    self.connectByCoords(x, y, x+1, y)
                if y > 0:
                    self.connectByCoords(x, y, x, y-1)
                if y < height - 1:
                    self.connectByCoords(x, y, x, y+1)

    def spanningTree(self):
        "Prim's algorithm, removes all possible edges, leaving all nodes accessible"
        pqueue = PriorityQueue()

        # add first node to the tree and its edges to the queue
        node = self.nodes[0]
        node.inTree = True
        for edge in node.edges:
            pqueue.put(edge)

        # until all nodes are in tree
        while not all(n.inTree for n in self.nodes):
            # get shortest edge leading outside of tree
            shortestEdge = None
            while True:
                shortestEdge = pqueue.get()
                if shortestEdge.inTree:
                    continue
                if not shortestEdge.node1.inTree:
                    node = shortestEdge.node1
                    break
                if not shortestEdge.node2.inTree:
                    node = shortestEdge.node2
                    break

            # add edge and node to the tree
            node.inTree = True
            shortestEdge.inTree = True

            # add all edges leading outside tree to the queue
            for edge in node.edges:
                if not edge.getOtherNode(node).inTree:
                    pqueue.put(edge)


if __name__ == '__main__':
    g = Graph()
    g.createGrid(5, 5)
    g.spanningTree()
