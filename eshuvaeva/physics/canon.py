import tkinter
import math

FPS = 5

CANVAS = tkinter.Canvas(width=1000, height=500)
CANVAS.pack()
STATE = {'v':100, 'angle': 50, 'g':10,'air':0.00000001}
PHYSICS_SYSTEM = {'air':STATE['air'],'x': 100, 'y': 100,'ay':STATE['air']* math.sin(STATE['angle']),'ax':STATE['air']* math.cos(STATE['angle']),'vx':STATE['v']* math.cos(STATE['angle']), 'vy':STATE['v']* math.sin(STATE['angle'])}

def make_step(physics_system, time_interval):
    PHYSICS_SYSTEM['ax'] = (PHYSICS_SYSTEM['vx']**2 )*STATE['air']
    PHYSICS_SYSTEM['ay'] = (PHYSICS_SYSTEM['vy']**2 )*STATE['air']
    PHYSICS_SYSTEM['x'] += PHYSICS_SYSTEM['vx'] * time_interval
    PHYSICS_SYSTEM['y'] += PHYSICS_SYSTEM['vy'] * time_interval
    PHYSICS_SYSTEM['vy'] += (STATE['g']-PHYSICS_SYSTEM['ay']) * time_interval
    PHYSICS_SYSTEM['vx'] = (PHYSICS_SYSTEM['vx']-PHYSICS_SYSTEM['ax']) * time_interval

def redraw(canvas, physics_system):
    canvas.create_oval(PHYSICS_SYSTEM['x'] - 2, PHYSICS_SYSTEM['y'] - 2, PHYSICS_SYSTEM['x'] + 2, PHYSICS_SYSTEM['y'] + 2, fill='black')

def loop():
    global STATE
    make_step(STATE, 1 / FPS)
    global CANVAS
    redraw(CANVAS, STATE)
    CANVAS.after(1000 // FPS, loop)


loop()
CANVAS.mainloop()
