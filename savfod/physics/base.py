import tkinter
import math

FPS = 24 #frames per second, i.e. how many step do you have in one second

CANVAS = tkinter.Canvas(width=500, height=300)
CANVAS.pack()

STATE = {'x':10, 'y':20} #write here parameters of your physical system

def make_step(state, time_interval):
    #write your function for changing state of physical system
    state['x'], state['y'] = state['x'] + time_interval * state['y'], state['y'] - time_interval * state['x']

def redraw(canvas, state):
    canvas.delete(*canvas.find_all())

    #write your function for drawing state of your physical system
    canvas.create_line(250, 150, 250 + state['x'], 150 + state['y'])
    canvas.create_oval(state['x'] + 250 - 5, state['y'] + 150 - 5, state['x'] + 250 + 5, state['y'] + 150 + 5, fill = 'green')

def loop():
    global STATE
    make_step(STATE, 1 / FPS)
    global CANVAS
    redraw(CANVAS, STATE)
    CANVAS.after(1000 // FPS, loop)

loop()
CANVAS.mainloop()
