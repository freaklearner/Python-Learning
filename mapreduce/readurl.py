import sys
sys.path.append(r'/usr/lib/python2.7/dist-packages')
import pandas
from pandas.tools.plotting import scatter_matrix;

def readurl(url):
    
    cols = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'];
    dataset = pandas.read_csv(url, names=cols)
    fl = open(r'repoData.txt','w')

    for row in dataset.to_records():
        st = str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+'\n'
        fl.write(st)
        #print(st)
    fl.close()
    print("successfully written in file repoData.txt")
