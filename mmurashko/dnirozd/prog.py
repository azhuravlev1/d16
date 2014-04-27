words=[]
d={}
dates={}

for a in open('name.txt','r'):
	a=a.split()
	words.append(a)
	d[a[1]]=a[0]

for b in open('surname.txt','r'):
	b=b.split()
	dates[b[0]]=b[1]
def names(x):
	return x[0]
words.sort(key=names)
with open('1.txt', 'w') as f_write:
	for x in words:
		f_write.write(x[0]+' '+x[1]+' '+dates[x[0]]+'\n')
