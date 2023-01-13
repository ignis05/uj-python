from graph import Graph
import tkinter as tk
import time


class CoordTranslator():
    "Helper class, translates node coordinates to real pixel values"

    def __init__(self, wChunk, hChunk, offset):
        self.width = wChunk
        self.height = hChunk
        self.offset = offset

    def topLeft(self, x, y):
        "Returns top left corner coordinates of a node with given coordinates"
        return self.offset + x * self.width, self.offset + y * self.height

    def botLeft(self, x, y):
        "Returns bottom left corner coordinates of a node with given coordinates"
        return self.offset + x * self.width, self.offset + (y+1) * self.height

    def topRight(self, x, y):
        "Returns top right corner coordinates of a node with given coordinates"
        return self.offset + (x+1) * self.width, self.offset + y * self.height

    def botRight(self, x, y):
        "Returns bottom right corner coordinates of a node with given coordinates"
        return self.offset + (x+1) * self.width, self.offset + (y+1) * self.height

    def leftWall(self, x, y):
        "Returns coordinates of two points, creating a left wall of a node with given coordinates"
        x1, y1 = self.topLeft(x, y)
        x2, y2 = self.botLeft(x, y)
        return x1, y1, x2, y2

    def rightWall(self, x, y):
        "Returns coordinates of two points, creating a right wall of a node with given coordinates"
        x1, y1 = self.topRight(x, y)
        x2, y2 = self.botRight(x, y)
        return x1, y1, x2, y2

    def topWall(self, x, y):
        "Returns coordinates of two points, creating a top wall of a node with given coordinates"
        x1, y1 = self.topLeft(x, y)
        x2, y2 = self.topRight(x, y)
        return x1, y1, x2, y2

    def botWall(self, x, y):
        "Returns coordinates of two points, creating a bottom wall of a node with given coordinates"
        x1, y1 = self.botLeft(x, y)
        x2, y2 = self.botRight(x, y)
        return x1, y1, x2, y2

    def center(self, x, y):
        "Returns coordinates of central point of a node with given coordinates"
        x1, y1 = self.topLeft(x, y)
        return x1+0.5*self.width, y1+0.5*self.height


def draw(
        w_chunks: int, h_chunks: int, canvas: tk.Canvas, drawPassages=False,
        drawTileNumbers=False):
    "Takes tk.Canvas and parameters from gui as arguments, and draws the labirynth"
    start = time.time()
    offset = 5
    width = canvas.winfo_width() - (2*offset)
    height = canvas.winfo_height() - (2*offset)
    wChunk = width/w_chunks
    hChunk = height/h_chunks

    print(f'drawing on cavas {width}x{height} ' +
          f'({w_chunks}*{wChunk}px)x({h_chunks}*{hChunk}px)')

    g = Graph()
    g.createGrid(w_chunks, h_chunks)
    g.spanningTree()

    canvas.delete("all")

    tr = CoordTranslator(wChunk, hChunk, offset)

    # left wall
    canvas.create_line(offset, offset, offset, offset+height, fill='black')
    # top wall
    canvas.create_line(offset, offset, offset+width, offset, fill='black')
    # right wall
    canvas.create_line(offset+width, offset, offset+width,
                       offset+height, fill='black')
    # bottom wall
    canvas.create_line(offset, offset+height, offset+width,
                       offset+height, fill='black')

    i = 0
    for y in range(h_chunks):
        for x in range(w_chunks):
            # right wall
            if x < w_chunks-1 and g.areCoordsConnected(x, y, x+1, y):
                if drawPassages:
                    canvas.create_line(*tr.rightWall(x, y), fill='yellow')
            else:
                canvas.create_line(*tr.rightWall(x, y), fill='black')

            # bottom wall
            if y < h_chunks-1 and g.areCoordsConnected(x, y, x, y+1):
                if drawPassages:
                    canvas.create_line(*tr.botWall(x, y), fill='yellow')
            else:
                canvas.create_line(*tr.botWall(x, y), fill='black')

            # tile numbers
            if drawTileNumbers:
                canvas.create_text(tr.center(x, y), text=f"{i}", fill="black")
            i += 1
    print(f'drawing done in {(time.time() - start)*1000 :.0f}ms')
