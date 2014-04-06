import turtle
turtle.speed('fastest')
ANGLE = 60
def koh(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        koh(length/3, depth-1)
        turtle.left(ANGLE)
        koh(length/3, depth-1)
        turtle.right(2*ANGLE)
        koh(length/3, depth-1)
        turtle.left(ANGLE)
        koh(length/3, depth-1)
koh(300, 4)
input()
