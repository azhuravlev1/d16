name = str(input())
file1 = str(input())
k =[]
def func(a):
	s = a[0].split()
	z = s[1]
	return z
f_read = open(name, 'r',encoding = 'utf8')
for line in f_read.readlines():
	line = line.strip()
	s = line.split(" ")
	k.append(s)
k = sorted(k,key = func)
print(k)
f_read.close()

f_read = open(file1, 'w')
for j in k:
	d = [';']
	m = j + d
	f_read.writelines(m)
f_read.close()
f_read = open(file1, 'r')
for line in f_read.readlines():
	line = line.strip()
	print(line)
f_read.close()
