import tkinter
import math
import random

FPS = 24 
CANVAS = tkinter.Canvas(width=800, height=500)
CANVAS.pack()

state = {'x':0, 'y':500, 'g':10, 'v': 300, 'angle': 0, 'vx': 10, 'vy':0, 'vwind': 10, 'anglewind': 0, 'vxwind': 0, 'vywind':0}
state['anglewind'] = random.random()
state['anglewind'] *= 100
state['vxwind'] = state['vwind']*math.cos(state['anglewind'])
state['vywind'] = state['vwind']*math.sin(state['anglewind'])
print(state['anglewind'])
def angle(event):
	a = event.x
	b = event.y
	tg = b/a
	state['angle'] = math.atan(tg)
	state['vx'] = state['v']*math.cos(state['angle'])
	state['vy'] = state['v']*math.sin(state['angle'])
	loop()


def make_step(state, time_interval):
    state['x'] += (state['vx']-state['vxwind'])*time_interval 
    state['y'] -= (state['vy']-state['vywind'])*time_interval
    state['vy'] -= state['g']
    if (state['x']) >= 800:
        state['vx'] = -state['vx'];
        state['vy'] = -state['vy'];
    if (state['y']) >= 500:
        state['y'] = 500;

def redraw(canvas, state):
    canvas.delete(*canvas.find_all())

    canvas.create_oval(state['x'] - 2, state['y'] - 2, state['x'] + 2, state['y'] + 2, fill='black')

def loop():
    global state
    make_step(state, 1 / FPS)
    global CANVAS
    redraw(CANVAS, state)
    CANVAS.after(1000 // FPS, loop)
CANVAS.bind('<Button-1>',angle)

CANVAS.mainloop()
