"""
domain_caller.py is designed to identify broad chromatin domain on the megabase scale.

v1.0
"""
########################################
#user specified gap size (d)
########################################
d=100
threshold=int(d/10)

########################################
#open input file and store in memory
########################################
outputfile=open('LAD_domains.bed','w')
with open("ladseq.bedgraph",'r') as f:
  data=f.readlines()
f.close()

data=[x.strip('\n').split() for x in data]
loop=1

########################################
#Main Program to call broad domains
########################################
for i in range(0,len(data),1):
    if (loop == 1 and float(data[i][3]) > 0): #will be first column of bedfile
        item=0
        holder=[]
        while item < d:
            holder.append(float(data[i+item][3]))
            item+=1
        if (sum(n<0 for n in holder)) == threshold:
            start=data[i][0]+'\t'+data[i][1]+'\t'
            outputfile.write(start)
            loop=0
    if (loop == 0 and float(data[i][3]) >0):
        continue
    if (loop == 0 and float(data[i][3]) <0): #ends domain and adds third column to bedfile
        end=data[i-1][2]
        outputfile.write(end+'\n')
        loop=1
outputfile.close()
