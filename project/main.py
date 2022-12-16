from draw import draw

import tkinter as tk


window = tk.Tk()

lbWidth = tk.Label(text="Width")
inWidth = tk.Entry()
lbWidth.pack()
inWidth.pack()

lbHeight = tk.Label(text="Height")
inHeight = tk.Entry()
lbHeight.pack()
inHeight.pack()

btDraw = tk.Button(text="Draw")
btDraw.pack()


def clickHandler(event):
    w = inWidth.get()
    h = inWidth.get()
    intW = int(w)
    intH = int(h)
    draw(w, h)


btDraw.bind("<Button-1>", clickHandler)


window.mainloop()
