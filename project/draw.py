from graph import Graph
import tkinter as tk


class CoordTranslator():
    def __init__(self, wChunk, hChunk, offset):
        self.width = wChunk
        self.height = hChunk
        self.offset = offset

    def topLeft(self, x, y):
        return self.offset + x * self.width, self.offset + y * self.height

    def botLeft(self, x, y):
        return self.offset + x * self.width, self.offset + (y+1) * self.height

    def topRight(self, x, y):
        return self.offset + (x+1) * self.width, self.offset + y * self.height

    def botRight(self, x, y):
        return self.offset + (x+1) * self.width, self.offset + (y+1) * self.height

    def leftWall(self, x, y):
        x1, y1 = self.topLeft(x, y)
        x2, y2 = self.botLeft(x, y)
        return x1, y1, x2, y2

    def rightWall(self, x, y):
        x1, y1 = self.topRight(x, y)
        x2, y2 = self.botRight(x, y)
        return x1, y1, x2, y2

    def topWall(self, x, y):
        x1, y1 = self.topLeft(x, y)
        x2, y2 = self.topRight(x, y)
        return x1, y1, x2, y2

    def botWall(self, x, y):
        x1, y1 = self.botLeft(x, y)
        x2, y2 = self.botRight(x, y)
        return x1, y1, x2, y2


def draw(w_chunks: int, h_chunks: int, canvas: tk.Canvas):
    g = Graph()
    g.createGrid(w_chunks, h_chunks)
    g.spanningTree()

    offset = 2
    width = canvas.winfo_width() - 2*offset
    height = canvas.winfo_height() - 2*offset
    wChunk = width/w_chunks
    hChunk = height/h_chunks

    print(f'drawing on cavas {width}x{height} ({w_chunks}*{wChunk}px)x({h_chunks}*{hChunk}px)')

    tr = CoordTranslator(wChunk, hChunk, offset)

    for y in range(h_chunks):
        for x in range(w_chunks):
            # left wall
            if x == 0 or not g.areCoordsConnected(x, y, x-1, y):
                canvas.create_line(*tr.leftWall(x, y), fill='black')
            # right wall
            if x == w_chunks-1 or not g.areCoordsConnected(x, y, x+1, y):
                canvas.create_line(*tr.rightWall(x, y), fill='black')
            # top wall
            if y == 0 or not g.areCoordsConnected(x, y, x, y-1):
                canvas.create_line(*tr.topWall(x, y), fill='black')
            # bottom wall
            if y == h_chunks-1 or not g.areCoordsConnected(x, y, x, y+1):
                canvas.create_line(*tr.botWall(x, y), fill='black')
