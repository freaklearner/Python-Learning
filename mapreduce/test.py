import pandas as pd
from hdfs import InsecureClient
import os

client_hdfs = InsecureClient('http://localhost:50070')

liste_hello =['hello1','hello2']
liste_world=['world1','world2']

df = pd.DataFrame(data= liste_hello+liste_world)

with client_hdfs.write('/user/temp/abcde.csv',encoding= 'utf-8') as writter:
 df.to_csv(writter)

print('data saved to hdfs ')


