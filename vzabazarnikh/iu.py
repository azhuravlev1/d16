import tkinter


c = tkinter.Canvas(width=1280, height=1024)
c.pack()
mach = 10



def onMouseClick(event):
    y = 0
    x = 0  
    t, k = event.x, event.y
    t = t
    k = k

    while y >= 0:
        c.create_line(x, y, x + t, y + k)
        x = x + t
        y = y + k
        k = k - 10



c.bind("<Button-1>", onMouseClick)
c.mainloop()

