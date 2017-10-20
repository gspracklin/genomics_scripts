"""
juicer_2_tadbit.py v1.0
By: George Spracklin

This script takes juicer_tools dump dense format and appends two columns (chr and bin position).
Output of this script is TADbit (find.tad() compatible)
"""

import os, sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:b:c:",["input=","output=","bin=","chromosome="])
    except getopt.GetoptError:
        print ('juicer_2_tadbit.py -i <inputfile> -o <outputfile> -b <bin size> -c <chromosome>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('juicer_2_tadbit.py -i <inputfile> -o <outputfile> -bin <bin size> -c <chromosome>')
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
        elif opt in ("-b", "--bin"):
            bin_size = int(arg)
        elif opt in ("-c", "--chromosome"):
            chromosome = arg
    print ('Input file is:', inputfile)
    print ('Output file is:', outputfile)
    print ('Bin size: ', bin_size)
    print ('chromosome: ', chromosome)
    juicer_2_tadbit(inputfile, outputfile, chromosome, bin_size)
    remove_NaN(outputfile)
    print('Removing temporary files')
    os.remove(outputfile)
    print('All finished')




def juicer_2_tadbit(inputfile, outputfile, chromosome, bin_size):
    print('Starting to add columns.')
    f = open(inputfile, 'r')
    w = open(outputfile, 'w')
    bin_size_start = 0
    for line in f:
        addition = str(chromosome) + '\t' + str(bin_size_start) + '-' + str(bin_size)
        w.write(addition + '\t' + line)
        bin_size_start += bin_size
        bin_size += bin_size
    f.close()
    w.close()
    return 'Finished with adding columns.'

def remove_NaN(outputfile):
    print('Starting to remove NaN')
    f1=open(outputfile,'r')
    f2=open(outputfile + '.mat', 'w')
    for line in f1:
        f2.write(line.replace('NaN', '0.0'))
    f1.close()
    f2.close()

if __name__ == "__main__":
   main(sys.argv[1:])
