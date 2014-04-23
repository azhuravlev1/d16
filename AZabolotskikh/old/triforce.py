try:
	import tkinter as T;
	isRunningOnMac = False;
except:
	import Tkinter as T;
	isRunningOnMac = True;

kScreenWidth = 1280;
kScreenHeight = 800;
kDockSize = 120;
kRecursionDepth = 10;
if (isRunningOnMac):
	kScreenHeight -= kDockSize;


C = T.Canvas(width = kScreenWidth, height = kScreenHeight, bg = '#000000');
C.pack();

def middle(x1,y1,x2,y2):
	return (x1+x2)/2,(y1+y2)/2;


def triforce(x1,y1,x2,y2,x3,y3,d, colour):
	if d == 0:
		if (not colour):
			fill = '#000000';
		else:
			fill ='#28FE14';
		C.create_polygon(x1,y1,x2,y2,x3,y3, fill = fill);
	else:
		xMiddleLeft, yMiddleLeft = middle(x1,y1,x2,y2);
		xMiddleBottom, yMiddleBottom = middle(x1,y1,x3,y3);
		xMiddleRight, yMiddleRight = middle(x2,y2,x3,y3);
		d -= 1;
		triforce(x1,y1,x2,y2,x3,y3,0,True);
		triforce(x1, y1, xMiddleLeft, yMiddleLeft, xMiddleBottom, yMiddleBottom, d, False);
		triforce(xMiddleLeft, yMiddleLeft, x2, y2, xMiddleRight, yMiddleRight, d, False);
		triforce(xMiddleBottom, yMiddleBottom, xMiddleRight, yMiddleRight, x3, y3,  d, False);


triforce(0,kScreenHeight,kScreenWidth/2,0,kScreenWidth,kScreenHeight,kRecursionDepth, False);
C.mainloop();
