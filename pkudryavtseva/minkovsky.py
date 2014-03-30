import turtle
turtle.speed('fastest')
ANGLE = 90
def line(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        line(length*0.25, depth-1)
        turtle.left(ANGLE)
        line(length*0.25, depth-1)
        turtle.right(ANGLE)
        line(length*0.25, depth-1)
        turtle.right(ANGLE)
        line(length*0.25, depth-1)
        line(length*0.25, depth-1)
        turtle.left(ANGLE)
        line(length*0.25, depth-1)
        turtle.left(ANGLE)
        line(length*0.25, depth-1)
        turtle.right(ANGLE)
        line(length*0.25, depth-1)
line(300, 3)
input() 
