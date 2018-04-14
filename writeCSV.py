from csv import reader,writer
import os
from os import path

#file_path = path.join(os.getcwd(),'files/repoData.txt')
#with open(file_path) as file:
#    csv_reader = reader(file)
#    data = [[s.upper() for s in row] for row in csv_reader]

#file_path = path.join(os.getcwd(),'files/test.csv')
#with open(file_path,'w') as file:
#    csv_writer = writer(file)
#    csv_writer.writerow(['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'])
#    for row in data:
#        csv_writer.writerow(row)

file_path = path.join(os.getcwd(),'files/repoData.txt')
with open(file_path) as file:
    csv_reader = reader(file)
    file_path = path.join(os.getcwd(),'files/test.csv')
    with open(file_path,'w') as file:
        csv_writer = writer(file)
        csv_writer.writerow(['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'])
        for row in csv_reader:
            csv_writer.writerow([s.upper() for s in row])

print('FILE SUCCESSFULLY WRITTEN')
