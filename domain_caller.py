"""
domain_caller.py is designed to identify broad chromatin domain on the megabase scale.

v2.0
"""
import os, sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:w:c:",["input=","output=","window=","chromosome="])
    except getopt.GetoptError:
        print('Input Error:')
        print ('domail_caller.py -i <inputfile> -o <outputfile> -w <window size> -c <chromosome>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('domain_caller.py v1.0 by George Spracklin')
            print('Usage:')
            print ('  domain_caller.py -i <inputfile> -o <outputfile> -w <window size> -c <chromosome>')
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
        elif opt in ("-w", "--window"):
            win_size = int(arg)
        elif opt in ("-c", "--chromosome"):
            chromosome = arg
    print ('Input file is:', inputfile)
    print ('Output file is:', outputfile)
    print ('Window size: ', win_size)
    print ('chromosome: ', chromosome)
    data = chr_split(inputfile)

    #Loop for all chromosomes
    if chromosome == 'all':
        mylist=[item[0] for item in data]
        mylist2=list(set(mylist))
        for item in sorted(mylist2):
            lyst=chromo(data, item)
            domain_caller(lyst, outputfile, win_size)
    #For an individual chromosomes
    else:
        lyst = chromo(data, chromosome)
        domain_caller(lyst, outputfile, win_size)

def chromo(data, chromosome):
    """Returns a chromosome specific list"""
    lyst=[]
    for i in range(0,len(data),1):
        if chromosome == str(data[i][0]):
            lyst.append(data[i])
    return lyst


def chr_split(inputfile):
    """Takes bedgraph and outputs dataframe - memory inefficient"""
    with open(inputfile,'r') as f:
      data=f.readlines()
    f.close()
    data=[x.strip('\n').split() for x in data ]
    return data


def domain_caller(lyst, outputfile, win_size):
    """input bedgraph, identify stretches of enriched signal, output bedfile"""
    if win_size < 5:
        print('Window size is too small for optimal use')
        return
    threshold=float(win_size/10) + 0.5
    if threshold > 10: threshold = 7 #caps upper limit on threshold
    print('Starting chr', lyst[0][0] )
    output_file=open(outputfile,'a')
    loop=1
    i=0
    for i in range(0,len(lyst),1):
        #Find the start of a domain
        if (loop == 1 and float(lyst[i][3]) > 0): #will be first column of bedfile
            item=-1
            holder=[]

            #Create list and check if domain is large
            while item < win_size:
                item+=1
                try:
                    holder.append(float(lyst[i+item][3]))
                except IndexError:
                    continue #might want to use Pass here
            #write start of large domain to file
            if (sum(n<0 for n in holder)) <= threshold:
                start=lyst[i][0]+'\t'+lyst[i][1]+'\t'
                output_file.write(start)
                loop=0

        #Start domain already started, keep going till negative value reached
        if (loop == 0 and float(lyst[i][3]) >0):
            continue

        #Find End of domain
        if (loop == 0 and float(lyst[i][3]) <0):
            diff_item=0
            diff_holder=[]
            while diff_item <= 5:
                diff_item+=1
                try:
                    diff_holder.append(float(lyst[i+diff_item][3]))
                except IndexError:
                    continue #might want to use Pass here
            if (sum(n<0 for n in diff_holder)) <= 2:
                continue
            elif (sum(n<0 for n in diff_holder)) > 2:
                end=lyst[i-1][2]
                output_file.write(end+'\n')
                loop=1
    #Add end of domain if lyst ends on row of positives
    if loop == 0:
        output_file.write(lyst[i][2]+'\n')
    output_file.close()

if __name__ == "__main__":
   main(sys.argv[1:])
