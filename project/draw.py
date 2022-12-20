from graph import Graph


def draw(width: int, height: int):
    print(f'drawing w:{width}, h:{height}')

    g = Graph()
    g.createGrid(width, height)
    g.spanningTree()


if __name__ == '__main__':
    draw(5, 5)