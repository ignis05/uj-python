from draw import draw

import tkinter as tk


root = tk.Tk()

lbWidth = tk.Label(text="Width")
inWidth = tk.Entry()
inWidth.insert(0, "25")
lbWidth.pack()
inWidth.pack()

lbHeight = tk.Label(text="Height")
inHeight = tk.Entry()
inHeight.insert(0, "25")
lbHeight.pack()
inHeight.pack()

drawPassages = tk.BooleanVar()
chbPass = tk.Checkbutton(root, text="Draw passages", variable=drawPassages)
chbPass.pack()

drawNumbers = tk.BooleanVar()
chbNumbers = tk.Checkbutton(root, text="Show tile numbers", variable=drawNumbers)
chbNumbers.pack()

btDraw = tk.Button(text="Draw")
btDraw.pack()

canv = tk.Canvas(root, bg="white", height=600, width=600)
canv.pack()


def clickHandler(event):
    w = int(inWidth.get())
    h = int(inWidth.get())
    dPass = drawPassages.get()
    dNo = drawNumbers.get()

    draw(w, h, canv, drawPassages=dPass, drawTileNumbers=dNo)


btDraw.bind("<Button-1>", clickHandler)


root.mainloop()
