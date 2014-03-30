import tkinter
c = tkinter.Canvas(width = 1000, height = 1000)
def serpinsky(depth, x1, y1, length, colour):
	if depth == 0:
		c.create_rectangle(x1, y1, x1+length, y1+length, fill = colour)
	else:
		serpinsky(depth-1, x1, y1, length/3, colour)
		serpinsky(depth-1, x1+length/3, y1, length/3, colour)
		serpinsky(depth-1, x1, y1+length/3, length/3, colour)
		serpinsky(depth-1, x1+length*2/3, y1, length/3, colour)
		serpinsky(depth-1, x1, y1+length*2/3, length/3, colour)
		serpinsky(depth-1, x1+length*2/3, y1+length*2/3, length/3, colour)
		serpinsky(depth-1, x1+length*2/3, y1+length/3, length/3, colour)
		serpinsky(depth-1, x1+length/3, y1+length*2/3, length/3, colour)
serpinsky(5, 0, 0, 800, 'red')
c.pack()
c.mainloop()
