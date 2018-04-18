from csv import writer
import os
from os import path

def writetweetsdata(time,leader,list):
    with open(path.join(os.getcwd(),'filescollection/tweetdata.csv'),'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([time,leader,list[0],list[1],list[2]])
