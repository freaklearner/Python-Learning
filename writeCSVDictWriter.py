from csv import DictWriter
import os

with open(os.path.join(os.getcwd(),'files/dictWrite.csv'),'w') as file:
    header = ['NAME','AGE']
    csv_writer = DictWriter(file,fieldnames=header)
    csv_writer.writeheader()
    write = True
    while write:
        print("Enter Name: ", end='')
        Name = input()
        print("Enter Age: ",end = '')
        Age = input()
        csv_writer.writerow({
            'NAME' : Name,
            'AGE'  : Age
        })
        print("Do you want more records to add(1/0): ",end = '')
        temp = input()
        if temp == '1':
            write = True
        else:
            write = False
