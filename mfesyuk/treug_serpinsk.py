import turtle
turtle.speed("fastest")
def treug(d, length):
    draw_serpinsky(d - 1, length/2)
    turtle.left(120)
    turtle.forward(length/2)
    draw_serpinsky(d - 1, length/2)
    turtle.left(120)
    turtle.forward(length/2)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length/2)
    turtle.left(120)
    draw_serpinsky(d - 1, length/2)
    turtle.forward(length/2)
def draw_serpinsky(length, d):
    if d == 0:
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
    else:
    treug(d, length)
draw_serpinsky(2, 200)
input()
