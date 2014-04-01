import turtle
turtle.speed('fastest')

ANGLE = 90

def draw_minkovsky(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        draw_minkovsky(length/4, depth-1)
        turtle.left(ANGLE)
        draw_minkovsky(length/4, depth-1)
        turtle.right(ANGLE)
        draw_minkovsky(length/4, depth-1)
        turtle.right(ANGLE)
        draw_minkovsky(length/4, depth-1)
        draw_minkovsky(length/4, depth-1)
        turtle.left(ANGLE)
        draw_minkovsky(length/4, depth-1)
        turtle.left(ANGLE)
        draw_minkovsky(length/4, depth-1)
        turtle.right(ANGLE)
        draw_minkovsky(length/4, depth-1)
draw_minkovsky(300, 3)
input()