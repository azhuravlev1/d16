import tkinter
import math

FPS = 100 #frames per second

WIDTH = 900
HEIGHT = 600
CANVAS = tkinter.Canvas(width=WIDTH, height=HEIGHT)
CANVAS.pack()
OBJECTS_TO_DEL = []

SPRINGS = [\
    {'stiffness': 1, 'x': 0, 'y': HEIGHT/2, 'length': WIDTH/2 }, \
    {'stiffness': 1, 'x': WIDTH, 'y': HEIGHT/2, 'length': WIDTH/2 }, \
    {'stiffness': 2, 'x': WIDTH/2, 'y': 0, 'length': HEIGHT/2 }, \
    {'stiffness': 2, 'x': WIDTH/2, 'y': HEIGHT , 'length': HEIGHT/2 }, \
]

BODY = {'x': 300, 'y': 200, 'velocity_x': 0, 'velocity_y': 0}

def calc_forces(body, spring):
    d_x = spring['x'] - body['x']
    d_y = spring['y'] - body['y']

    length = math.sqrt(d_x**2 + d_y**2)
    d_length = length - spring['length']
    force = d_length * spring['stiffness']

    force_x = force * d_x / length
    force_y = force * d_y / length

    return force_x, force_y

def make_step(body, time_interval):
    body['x'] += body['velocity_x'] * time_interval
    body['y'] += body['velocity_y'] * time_interval

    force_x, force_y = 0, 0
    for spring in SPRINGS:
        force_x += calc_forces(body, spring)[0]
        force_y += calc_forces(body, spring)[1]
    body['velocity_x'] += force_x * time_interval
    body['velocity_y'] += force_y * time_interval


def redraw(canvas, body):
    global OBJECTS_TO_DEL
    for obj in OBJECTS_TO_DEL:
        canvas.delete(obj)

    canvas.create_oval(body['x'] - 2, body['y'] - 2, body['x'] + 2, body['y'] + 2, fill='black')

    OBJECTS_TO_DEL = []
    for spring in SPRINGS:
        OBJECTS_TO_DEL.append(canvas.create_line(body['x'], body['y'], spring['x'], spring['y']))
        force_x, force_y = calc_forces(body, spring)
        OBJECTS_TO_DEL.append(canvas.create_line(body['x'], body['y'], body['x'] + force_x, body['y'] + force_y, fill='green'))


def loop():
    global BODY
    make_step(BODY, 1 / FPS)
    global CANVAS
    redraw(CANVAS, BODY)
    CANVAS.after(1000 // FPS, loop)

def change_start_point(event):
    global BODY
    BODY['x'] = event.x
    BODY['y'] = event.y
    BODY['velocity_y'] = BODY['velocity_x'] = 0
    global CANVAS
    CANVAS.delete(*CANVAS.find_all())

loop()

CANVAS.bind('<Button-1>', change_start_point)
CANVAS.mainloop()
