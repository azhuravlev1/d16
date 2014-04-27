import sys
fr=sys.argv[1]
fw=sys.argv[2]
a = []

with open(fr,'r') as f_read:
	for line in f_read:
		line = line.strip().split()
		for x in line:
			with open(fw,'w') as f_w:
				f_w.writelines(x)
				a.append(x)
f_read.close()
f_w.close()
def length(x):
	return len(x)
a = sorted(a,key = length)
print(a)
