import tkinter
c = tkinter. Canvas (width = 900, height = 900)
c.pack()
def draw_serp(length, x, y, canvas, n, max_n):
	if n == 0:
		canvas.create_rectangle(x, y, x + length, x + length, fill = 'green')
		draw_serp(length, x, y, canvas, 1, max_n)
		return
	if n != max_n and n != 0:
		canvas.create_rectangle(x + (length / 3), y + (length / 3), x + (2 * length / 3), y + (2 * length / 3), fill = 'white')
		draw_serp(length / 3, x, y, canvas, n + 1, max_n)
		draw_serp(length / 3, x + (length / 3), y, canvas, n + 1, max_n)
		draw_serp(length / 3, x + (2 * length / 3), y, canvas, n + 1, max_n)
		draw_serp(length / 3, x, y + (length / 3), canvas, n + 1, max_n)
		draw_serp(length / 3, x + (2 * length / 3), y + (length / 3), canvas, n + 1, max_n)
		draw_serp(length / 3, x, y + (2 * length / 3), canvas, n + 1, max_n)
		draw_serp(length / 3, x + (length / 3), y + (2 * length / 3), canvas, n + 1, max_n)
		draw_serp(length / 3, x + (2 * length / 3), y + (2 * length / 3), canvas, n + 1, max_n)
		return
	if n == max_n:
		return

draw_serp(900, 0, 0, c, 0, 5)

c.mainloop()		
