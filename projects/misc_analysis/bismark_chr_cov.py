o = input("what file?: " )
f = open(o, 'r')
newfile = open('chr_'+o,'w')

for line in f:
    newfile.write(''.join('chr'+line))

f.close()
newfile.close()
