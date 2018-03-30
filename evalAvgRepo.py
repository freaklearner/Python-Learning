import sys
sys.path.append(r'/usr/lib/python2.7/dist-packages/')
import numpy as nm

f1 = open(r'files/repoData.txt','r')

label = []
data = {}
for x in f1.readlines():
    ar = x.split(',')
    if not ar[4] in label:
        label.append(str(ar[4]))
        data[str(ar[4])] = []
    data[str(ar[4])].append(float(ar[1]))

for lb,val in data.items():
    av = nm.average(list(val))
    print("%s Average : %f"%(lb,av))
        
