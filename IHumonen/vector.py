n=int(input())
shape=[]
for i in range (n):
	vector=input()
	vector=vector.split()
	vector1=[int(vector[0]), int(vector[1])]
	shape.append(vector1)
otvet=0
def area(x, y):
	global otvet
	len1=(shape[x][0]**2+shape[x][1]**2)**(-2)
	len2=(shape[y][0]**2+shape[y][1]**2)**(-2)
	len3=((shape[x][0]-shape[y][0])**2+(shape[x][1]-shape[y][1])**2)**(-2)
	cos=(len1**2+len2**2-len3**2)/(2*len1*len2)
	sin=(1-cos**2)**(-2)
	_area_=len1*len2*sin
	otvet+=_area_
for i in range (n-1):
	area(i, i+1)
area(n-1, 0)
print(otvet/2)