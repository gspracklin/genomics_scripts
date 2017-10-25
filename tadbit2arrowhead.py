

inputfile = input('tadbit file: ')
bin_size = int(input('bin size: '))
outputfile=input('Outputfile name: ')
chromosome=input('chromosome: ')
f = open(inputfile, 'r')
w = open(outputfile, 'w')
w.write('chr1'+'\t'+'x1'+'\t'+'x2'+'\t'+'chr2'+'\t'+'y1'+'\t'+'y2'+'\t'+\
'color'+'\t'+'density'+'\t'+'score'+'\n')
color = str(255)+','+str(255)+','+str(0)


for line in f:
    z=line.split()
    try:
        if z[0].isdigit() == True:
            start= str((int(z[1])-1) * bin_size)
            end = str((int(z[2]))   * bin_size)
            size = str(chromosome)+'\t'+str(start)+'\t'+str(end)+\
            '\t'+str(chromosome)+'\t'+str(start)+'\t'+str(end)+'\t'\
            +color+'\t'+str(z[3])+'\n' #'\t'+str(z[4])+
            w.write(size)
    except IndexError: pass

f.close()
w.close()


#catch IndexError: list index out of range
