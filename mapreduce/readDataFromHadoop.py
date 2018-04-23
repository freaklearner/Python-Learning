import pandas
from hdfs import InsecureClient
import os
from csv import reader

client_hdfs = InsecureClient('http://localhost:50070')

client_hdfs.

with client_hdfs.read('/user/hdfs/wiki/helloworld.csv', encoding = 'utf-8',) as reader:
    df = pd.read_csv(reader,index_col=0)
#with client_hdfs.write('/user/temp/repourldata.csv',encoding='utf-8') as writer:
#    df.to_csv(writer)

print('SUCCESSFULL RUN')
