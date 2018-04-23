import pandas
from hdfs import InsecureClient
import os
from csv import reader

client_hdfs = InsecureClient('http://localhost:50070')
file_path = os.path.join(os.getcwd(),'filescollection/tweetdata.csv')
print(file_path)
with open(file_path) as file:
    csv_reader = reader(file)
    df = pandas.DataFrame([row for row in file])
    print(df.describe())
with client_hdfs.write('/user/sentimentAnly.csv',encoding='utf-8') as writer:
    df.to_csv(writer)

print('SUCCESSFULL RUN')
