import tkinter
import math

FPS = 2 #frames per second

CANVAS = tkinter.Canvas(width=500, height=300)
CANVAS.pack()

PHYSICS_SYSTEM = []

def make_step(physics_system, time_interval):
    pass

def redraw(canvas, physics_system):
    pass

def loop():
    global PHYSICS_SYSTEM
    make_step(PHYSICS_SYSTEM, 1 / FPS)
    global CANVAS
    redraw(CANVAS, PHYSICS_SYSTEM)
    CANVAS.after(1000 // FPS, loop)


loop()
CANVAS.mainloop()
