

filename = input('what input filename?')
file_open = open(filename, 'r')
newfilename = input('what output filename?')
newfile = open(newfilename, 'w')
chr = input('what chromosome?')
for line in file_open:
    z = line.split()
    chromosome = str('chr'+chr)
    if z[0] == chromosome:
        newfile.write(line)

file_open.close()
newfile.close()
