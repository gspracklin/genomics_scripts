# Bioinformatic scripts-
Various scripts to change fasta files (i.e. headers, chromosome separators, etc...)

matrix.py converts TADbit matrix files (.mat) to BUTLRTools format 

bismark_chr_cov.py adds 'chr' to bismark .cov files that were aligned without 'chr' in the reference genome

basemods_separator.py parses GFF files based on base modification (i.e. PacBio modifications - m6A, m4C etc...) 

juicer_2_tadbit.py takes juicer_tools dump dense matrix and appends chromosome column and bin position, making file compatible with TADbit find.tads()

singlecell_DamID.py takes scDamID data from Kind et al., 2015 Cell and aggregates data into bedgraph format using numpy

domain_caller.py takes bedgraph files and calls megabase sized domains
