"""
domain_caller.py is designed to identify broad chromatin domain on the megabase scale.

v1.0
"""
import os, sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:w:",["input=","output=","window="])
    except getopt.GetoptError:
        print ('domail_caller.py -i <inputfile> -o <outputfile> -w <window size>')
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
#        elif opt in ("-c", "--chromosome"):
#            chromosome = arg
    print ('Input file is:', inputfile)
    print ('Output file is:', outputfile)
    print ('Window size: ', win_size)
#    print ('chromosome: ', chromosome)
    domain_caller(inputfile, outputfile, win_size)
#    os.remove(outputfile)
    print('All finished')


########################################
#Main Program to call broad domains
########################################
def domain_caller(inputfile, outputfile, win_size=100):
    threshold=int(win_size/10)
    print('the window size is: ', win_size)
    print('the threshold is: ', threshold)
    output_file=open(outputfile,'w')
    with open(inputfile,'r') as f:
      data=f.readlines()
    f.close()
    data=[x.strip('\n').split() for x in data]
    loop=1
    print('starting for loop')
    for i in range(0,len(data),1):
        if (loop == 1 and float(data[i][3]) > 0): #will be first column of bedfile
            item=0
            holder=[]
            while item < win_size:
                holder.append(float(data[i+item][3]))
                item+=1
            if (sum(n<0 for n in holder)) == threshold:
                start=data[i][0]+'\t'+data[i][1]+'\t'
                output_file.write(start)
                loop=0
        if (loop == 0 and float(data[i][3]) >0):
            continue
        if (loop == 0 and float(data[i][3]) <0): #ends domain and adds third column to bedfile
            end=data[i-1][2]
            output_file.write(end+'\n')
            loop=1
    output_file.close()

if __name__ == "__main__":
   main(sys.argv[1:])
