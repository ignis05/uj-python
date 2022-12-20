from draw import draw

import tkinter as tk


root = tk.Tk()

lbWidth = tk.Label(text="Width")
inWidth = tk.Entry()
inWidth.insert(0, "10")
lbWidth.pack()
inWidth.pack()

lbHeight = tk.Label(text="Height")
inHeight = tk.Entry()
inHeight.insert(0, "10")
lbHeight.pack()
inHeight.pack()

btDraw = tk.Button(text="Draw")
btDraw.pack()

canv = tk.Canvas(root, bg="white", height=500, width=500)
canv.pack()

def clickHandler(event):
    w = inWidth.get()
    h = inWidth.get()
    intW = int(w)
    intH = int(h)

    draw(intW, intH, canv)


btDraw.bind("<Button-1>", clickHandler)


root.mainloop()
