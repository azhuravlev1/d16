import turtle
import tkinter
turtle.speed(fastest)
def qwe(a1, a2, a3):
	if a1 > 0:
		qwe(a1 - 1, a2 / 3, a3)
		turtle.right(a3)
		qwe(a1 - 1, a2 / 3, a3)
		turtle.left(a3 * 2)
		qwe(a1 - 1, a2 / 3, a3)
		turtle.right(a3)
		qwe(a1 - 1, a2 / 3, a3)
	if a1 == 0:
		turtle.forward(a2)	

def rty(a1, a2): 
	qwe(a1, a2, 60) 
	turtle.left(120)
	qwe(a1, a2, 60)
	turtle.left(120) 
	qwe(a1, a2, 60)

turtle.backward(200)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
rty(2,400)
input()