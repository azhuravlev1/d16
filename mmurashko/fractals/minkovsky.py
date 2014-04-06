import turtle

def draw_minkovskiy(length, depth):
	if depth==0:
		turtle.forward(length)
	else:
		draw_minkovskiy(length/4,depth-1)
		turtle.left(90)
		draw_minkovskiy(length/4,depth-1)
		turtle.right(90)
		draw_minkovskiy(length/4,depth-1)
		turtle.right(90)
		draw_minkovskiy(length/2,depth-1)
		turtle.left(90)
		draw_minkovskiy(length/4,depth-1)
		turtle.left(90)
		draw_minkovskiy(length/4,depth-1)
		turtle.right(90)
		draw_minkovskiy(length/4,depth-1)
l=int(input())#for example 300
d=int(input())#for example 3
turtle.speed('fastest')
draw_minkovskiy(l,d)
input()
