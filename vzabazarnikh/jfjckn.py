im = open('imena.txt', 'r', encoding = "utf8").read()
im = im.strip()
im = im.sort()

dat = open('dat.txt', 'r', encoding = "utf8").read()
dat = dat.strip()
dat = dat.sort()
h = [""]*len(im)

for x in range(len(im)):
    i = im[x]
    i = i.split
    d = dat[x]
    d = d.split
    f = [""]*3
    f[0] = i[0]
    f[1] = d[1]
    f[2] = i[1]
    h[x] = f

with open('dat.txt', 'w') us tg:
    tg.write('h\n')


 
