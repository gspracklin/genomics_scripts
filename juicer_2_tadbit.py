"""
juicer_2_tadbit.py v1.0
By: George Spracklin

This script takes juicer_tools dump dense format and appends two columns (chr and bin position).
Output of this script is TADbit (find.tad() compatible)
"""


matrix_file = open('chr11_dense.txt', 'r')
output = input('what to call file? ')
tadbit_file = open(output, 'w')
interval = int(input('what is the bin size? (in bp) '))
chromosome = int(input('what is chromosome? (# only) '))

bin_size_start = 0
bin_size_end = interval


for line in matrix_file:
    addition = str(chromosome) + '\t' + str(bin_size_start) + '-' + str(bin_size_end)
    tadbit_file.write(addition + '\t' + line)
    bin_size_start += interval
    bin_size_end += interval


matrix_file.close()
tadbit_file.close()
