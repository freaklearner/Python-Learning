from csv import reader
from hdfs import InsecureClient
import pandas
from os import path
import os

client_hdfs = InsecureClient('http://localhost:50070')
file_path  = path.join(os.getcwd(),'filescollection/wordscount.csv')
print(file_path)
with open(file_path) as file:

    csv_reader = reader(file)

    data_frame = pandas.DataFrame([row for row in csv_reader])
    print(data_frame)
with client_hdfs.write('/user/temp/wordscount.csv', encoding='utf-8') as writer:
    data_frame.to_csv(writer)

print("SUCCESSFULL EXECUTED")
