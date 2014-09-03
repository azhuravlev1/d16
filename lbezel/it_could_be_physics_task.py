import tkinter
import math
from sys import argv

if len(argv) > 2:
    kWidth = int(argv[1])
    kHeight = int(argv[2])
else:
    kWidth = 900
    kHeight = 600

FPS = 40 #frames per second, i.e. how many step do you have in one second
CANVAS = tkinter.Canvas(width=kWidth, height=kHeight)
CANVAS.pack()
CANVAS.create_polygon(0, kHeight, 0, 0, kWidth, 0, kWidth, kHeight, fill = "yellow")

STATE = {'x':170, 'y':100} #write here parameters of your physical system
state0 = {'x':42, 'y':10}
def make_step(state, state0, time_interval):
    #write your function for changing state of physical system
    x = state['x']
    y = state['y']
    a = state0['x']
    b = state0['y']
    state0['x'] = x
    state0['y'] = y
    t = time_interval
    print(x,y,a,b)
    if x >= a and y <= b and x <= kWidth and y >= 0 or  y >= kHeight and x >= a   or x <= 0 and y >= b   :
        x, y = x + t*y, y - t*x
    elif x >= a and y >= b and x <= kWidth and y <= kHeight and x >= 0 and y >= 0 or x <= 0 and y <= b  or  y <= 0 and x <= a   :
        x, y = x + t*y, y + t*x
    elif x <= a and y <= b and x >= 0 and y >= 0 or  x >= kWidth and y <= b or y >= kHeight and x <= a       :
        x, y = x - t*y, y - t*x
    elif x <= a and y >= b and x >= 0 and y <= kHeight or    y <= 0 and x >= a   or   x >= kWidth and y >= b  :
        x, y = x - t*y, y + t*x

    state['x'] = x
    state['y'] = y
    time_interval = t + 1/FPS
def redraw(canvas, state):
    #canvas.delete(*canvas.find_all())
    #write your function for drawing state of your physical system
    #canvas.create_oval(1,1,100,100)
    canvas.create_oval(state['x'] - 1, state['y'] - 1, state['x'] + 1, state['y'] + 1, fill = 'black')
def loop():
    global STATE
    for i in range(100):
        make_step(STATE, state0, 1 / (FPS * 100) )
    global CANVAS
    redraw(CANVAS, STATE)
    CANVAS.after(100 // FPS, loop)
loop()
CANVAS.mainloop()
