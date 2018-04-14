from csv import reader
from os import path
import os
with open(path.join(os.getcwd(),'files/repoData.txt')) as file:
    csv_reader = reader(file, delimiter=',' )
    csv_reader = list(file)
    for row in csv_reader:
        print(row)
