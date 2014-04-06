import turtle
turtle.speed("fastest")
def draw_levi(d, length):
	if d == 0:
		turtle.forward(length)	
	else:
		draw_levi(d - 1, length / 3)
		turtle.left(60)
		draw_levi(d - 1, length / 3)
		turtle.right(120)
		draw_levi(d - 1, length / 3)
		turtle.left(60)
		draw_levi(d - 1, length / 3)
draw_levi(4, 200)
input()
