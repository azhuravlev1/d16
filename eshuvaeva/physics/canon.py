import tkinter
import math

FPS = 2 #frames per second

CANVAS = tkinter.Canvas(width=500, height=500)
CANVAS.pack()
PHYSICS_SYSTEM = {'v':100, 'angle': 1, 'g':10, 'air':5}
body = {'x': 800, 'y': 800,'vx':PHYSICS_SYSTEM['v']* math.cos(PHYSICS_SYSTEM['angle']), 'vy':PHYSICS_SYSTEM['v']* math.sin(PHYSICS_SYSTEM['angle'])}

def make_step(physics_system, time_interval):
    body['x'] += body['vx'] * time_interval
    body['y'] += body['vy'] * time_interval
    body['vy'] += PHYSICS_SYSTEM['g'] * time_interval

def redraw(canvas, physics_system):
    canvas.create_oval(body['x'] - 2, body['y'] - 2, body['x'] + 2, body['y'] + 2, fill='black')

def loop():
    global PHYSICS_SYSTEM
    make_step(PHYSICS_SYSTEM, 1 / 5 * FPS)
    global CANVAS
    redraw(CANVAS, PHYSICS_SYSTEM)
    CANVAS.after(1000 // FPS, loop)


loop()
CANVAS.mainloop()

