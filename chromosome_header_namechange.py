"""
This script changes the header of fasta files to just the chromosome number.
i.e. '>chr10 dna_sm:chromosome chromosome:GRCh38:1:1:248956422:1 REF'
 will be '>10'
"""
fasta = input('Input genome file')
new_fasta = input('Input new genome filename')
f = open(fasta, 'r')
genome = open(new_fasta, 'w')

for line in f:
    if '>' in line:
        y = line[1:]
        x = y.split()
        z = '>' + str(x[0]) + '\n'
        genome.write(z)
    else: genome.write(line)
f.close()
genome.close()
