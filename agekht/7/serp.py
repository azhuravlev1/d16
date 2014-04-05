import tkinter
c = tkinter.Canvas(width = 800, height = 600)
def kovser(dep, a1, a2, l, color):
	if dep == 0:
		c.create_rectangle(a1, a2, a1 + l, a2 + l, fill = color)
	else:
		kovser(dep - 1, a1, a2, l / 3, color) 
		kovser(dep - 1, a1 + l / 3, a2, l / 3, color)
		kovser(dep - 1, a1, a2 + l / 3, l / 3, color)
		kovser(dep - 1, a1 + l * 2 / 3, a2, l / 3, color)
		kovser(dep - 1, a1, a2 + l * 2 / 3, l / 3, color)
		kovser(dep - 1, a1 + l * 2 / 3, a2 + l * 2 / 3, l / 3, color)
		kovser(dep - 1, a1 + l * 2 / 3, a2 + l / 3, l / 3, color)
		kovser(dep - 1, a1 + l / 3, a2 + l * 2 / 3, l / 3, color)
		
kovser(5, 0, 0, 1000, 'navy')
c.pack()
c.mainloop()