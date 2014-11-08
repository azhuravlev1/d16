import tkinter
WIDTH=1000
HEIGHT=900
def distance (x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def par(x1,y1,x2,y2,x3,y3):
    a=(y3*(x2-x1)+y1*(x3-x2)+y2*(x1-x3))/(x3-x1)/(x3-x2)/(x2-x1)
    b=(y3-y1)/(x3-x1)-a*(x1+x3)
    c=y1-a*x1**2-b*x1
    return(a,b,c)
def f(a,b,c,x):
    return a*x**2+b*x+c
def draw_par(x1,y1,x2,y2,x3,y3,X1,X2,tf,can):
    l=0
    k=40
    s=abs(X1-X2)/k
    a,b,d=par(x1,y1,x2,y2,x3,y3)
    if tf==True and 1==2:
        can.create_oval(x1-10,y1-10,x1+10,y1+10,fill='red')
        can.create_oval(x2-10,y2-10,x2+10,y2+10,fill='red')
        can.create_oval(x3-10,y3-10,x3+10,y3+10,fill='red')
    for i in range(0,k):
        if tf==True:
            can.create_line(X1+s*i,f(a,b,d,X1+s*i),X1+s*(i+1),f(a,b,d,X1+s*(i+1)))
        l+=distance(X1+s*i,f(a,b,d,X1+s*i),X1+s*(i+1),f(a,b,d,X1+s*(i+1)))
    return l
def draw_rope(x1,y1,x2,y2,l,can):
    X=(x1+x2)/2
    S=[(y1+y2)/2,(y1+y2)/2+l/2]
    Y=(S[0]+S[1])/2
    while abs(draw_par(x1,y1,x2,y2,X,Y,x1,x2,False,can)-l)>0.1:
        if  draw_par(x1,y1,x2,y2,X,Y,x1,x2,False,can)>l:
            S=[S[0],(S[0]+S[1])/2]
            Y=(S[0]+S[1])/2
        else:
            S=[(S[0]+S[1])/2,S[1]]
            Y=(S[0]+S[1])/2
    draw_par(x1,y1,x2,y2,X,Y,x1,x2,True,can)
                
