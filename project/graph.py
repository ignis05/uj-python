from queue import PriorityQueue
from random import randint


class GraphEdge:
    def __init__(self, node1, node2, weight: int):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
        self.inTree = False

    def getOtherNode(self, node):
        if self.node1 == node:
            return self.node2
        else:
            return self.node1


class GraphNode:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.edges: list[GraphEdge] = []
        self.inTree = False

    @property
    def getNeighbors(self):
        return [edge.getOtherNode(self) for edge in self.edges]


class Graph:
    def __init__(self):
        self.nodes: list[GraphNode] = []

    def addNode(self, x: int, y: int):
        node = GraphNode(x, y)
        self.nodes.append(node)
        return node

    def connect(self, node1: GraphNode, node2: GraphNode, weight: int = 1):
        for edge in node1.edges:
            if edge.getOtherNode(node1) == node2:
                return

        edge = GraphEdge(node1, node2, weight)
        node1.edges.append(edge)
        node2.edges.append(edge)

    def find(self, x, y):
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node

    def areCoordsConnected(self, x1, y1, x2, y2):
        node1 = self.find(x1, y1)
        node2 = self.find(x2, y2)
        for edge in node1.edges:
            if edge.getOtherNode(node1) == node2:
                return True
        return False

    def connectByCoords(self, x1, y1, x2, y2):
        self.connect(self.find(x1, y1), self.find(x2, y2), randint(0, 10000))

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
                if y < width - 1:
                    self.connectByCoords(x, y, x, y+1)

    def spanningTree(self):
        "Prim's algorithm, removes all possible edges, leaving all vertexes accessible"
        pqueue = PriorityQueue()

        # add first node to the tree and its edges to the queue
        node = self.nodes[0]
        node.inTree = True
        for edge in node.edges:
            pqueue.put((edge.weight, edge, node))

        # each iteration add one node to the tree
        for i in range(1, len(self.nodes)):
            # get shortest edge leaning outside of tree
            shortestEdge = None
            while True:
                _, shortestEdge, startNode = pqueue.get()
                node = shortestEdge.getOtherNode(startNode)
                if shortestEdge.inTree == False:
                    break

            # add edge and node to the tree
            node.inTree = True
            shortestEdge.inTree = True

            # add all edges leading outside tree to the queue
            for edge in node.edges:
                if not edge.getOtherNode(node).inTree:
                    pqueue.put((edge.weight, edge, node))

        # remove edges not in tree
        for node in self.nodes:
            for edge in node.edges:
                if not edge.inTree:
                    node.edges.remove(edge)

        # reset inTree values
        for node in self.nodes:
            node.inTree = False
            for edge in node.edges:
                edge.inTree = False


if __name__ == '__main__':
    g = Graph()
    g.createGrid(5, 5)
    g.spanningTree()
