import pandas as pd
from hdfs import InsecureClient
import os

client_hdfs = InsecureClient('http://localhost:50070')

#liste_hello =['hello1','hello2','hello3']
#liste_world=['world1','world2']
f1 = open('wordscount.txt')
content = []
for line in f1.readlines():
	line = line.split()
	line = unicode(line[0],'utf-8')
	content.append(line)
#print(content)
df = pd.DataFrame(data=content)
print(df)
print(df.shape)
print(df.head(n=2))
f1.close()

with client_hdfs.write('/user/temp/wordscount.csv',encoding='utf8') as writter:
 df.to_csv(writter)

print('data saved to hdfs ')
