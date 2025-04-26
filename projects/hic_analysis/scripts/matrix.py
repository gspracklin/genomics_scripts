

f = open('10.mat', 'r')

newfile = open('10_new.mat', 'w')
for line in f:
    y = line.split()
    if '#' and 'MASKED' in y:
        continue
    else:
        alist = y[2:]
        blist = ('\t'.join(map(str,alist)))
        newfile.write(blist)
        newfile.write('\n')

f.close()
newfile.close()
