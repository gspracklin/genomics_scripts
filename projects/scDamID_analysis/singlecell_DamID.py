"""
singlecell_DamID.py converts scDamID data into bedgraph format
compatible with IGV

George Spracklin
v1.0
"""
import numpy as np

inputfile=open("DataS5_Clone.5-8(Dam_only).1N.OE.txt", 'r')
outputfile=open('DataS5_Clone.5-8(Dam_only).1N.OE.bedgraph', 'w')

for line in inputfile:
    z=line.split()
    if 'chr' in z[0]: #remove header
        if 'NA' in z: #numpy mean can't have NA
            continue
        else:
            header=z[0]+'\t'+z[1]+'\t'+z[2]+'\t' #genomic coordinates
            outputfile.write(header)
            array=np.array(z[3:]).astype(np.float) #create numpy array
            value=np.mean(array) #note: zeros are included in value, debatable whether they should be included
            ratio = str(value)+'\n'
            outputfile.write(ratio)

inputfile.close()
outputfile.close()
