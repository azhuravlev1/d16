def f (x):
	return x	

def g (x):
	return x**2

h=lambda x:(1-x**2)**(1/2)

def trapezium_integral(a, b, f):
	dx=(b-a)/10000
	es=0
	for i in range(10000):
		l=(f((i+1)*dx+a)-f(i*dx+a))/2.+f(i*dx+a)
		s=dx*l
		es=es+s
	return es

print(trapezium_integral(2, 3, f))
print(trapezium_integral(0, 1, g))
print(2*(trapezium_integral(-1, 1, h)))
