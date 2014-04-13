import tkinter
import math

FPS = 2 #frames per second

CANVAS = tkinter.Canvas(width=1000, height=500)
CANVAS.pack()
PHYSICS_SYSTEM = {'v':100, 'angle': 50, 'g':10,'air':0.0001}
body = {'air':PHYSICS_SYSTEM['air'],'x': 100, 'y': 100,'vx':PHYSICS_SYSTEM['v']* math.cos(PHYSICS_SYSTEM['angle']), 'vy':PHYSICS_SYSTEM['v']* math.sin(PHYSICS_SYSTEM['angle'])}

def make_step(physics_system, time_interval):
    body['air'] += (body['vx']**2 + body['vy']**2)*PHYSICS_SYSTEM['air']
    body['x'] += (body['vx']-body['air']) * time_interval
    body['y'] += (body['vy']-body['air']) * time_interval
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
