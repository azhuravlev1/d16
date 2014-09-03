import tkinter
c=tkinter.Canvas(width=1000,height=1000)
c.pack()
n=5
c.create_line(0, 1000, 500, 0)
c.create_line(500, 0, 1000, 1000)
c.create_line(1000, 1000, 0, 1000)
def mddl_trngl(x1, x2, x3, y1, y2, y3, i):
    if i<n:
        xn1=(x1+x2)/2
        xn2=(x3+x2)/2
        xn3=(x1+x3)/2
        yn1=(y1+y2)/2
        yn2=(y3+y2)/2
        yn3=(y1+y3)/2
        c.create_line(xn1, yn1, xn2, yn2, xn3, yn3, xn1, yn1,)
        i+=1
        mddl_trngl(x1, xn1, xn3, y1, yn1, yn3, i)
        mddl_trngl(xn1, x2, xn2, yn1, y2, yn2, i)
        mddl_trngl(xn3, xn2, x3, yn3, yn2, y3, i)
mddl_trngl(0, 500, 1000, 1000, 0, 1000, 0)
c.mainloop()
