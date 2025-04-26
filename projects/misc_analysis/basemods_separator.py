"""
This script parses GFF files based on basemods
"""


gff = input("what is the gff file?: ")
mod = input("what is the modification?: ")
read_gff = open(gff, 'r')
output_gff = open(mod + '_' + gff, 'w')


for line in read_gff:
    read = line.split()
    if 'chr17' in read[0]:
        if mod in read[2]:
            output_gff.write(line)
read_gff.close()
output_gff.close()
