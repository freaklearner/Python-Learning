import os
from os import path
import extractwordsfile as ewf
import reducer as rd
import mapper as m
from csv import writer
import replaceCharacter as rc
files_path =  path.join(os.getcwd(),'filescollection')  #str(os.getcwd()) + '/filescollection'
#print(files_path)
files = [f for f in os.listdir(files_path) if path.isfile(path.join(files_path,f))]
content = []
for fl in files:
    pt = path.join(files_path,fl)
    #rc.replaceChar(pt,"'",'"') 
    content.extend(ewf.extractwordsfromfile(pt))
dic = rd.reducer(content)
fl = path.join(os.getcwd(),'filescollection/wordscount.csv')
with open(fl,'w') as file:
    csv_write = writer(file)
    csv_write.writerow(['WORDS','COUNT'])
    for key,value in dic.items():
        if len(key) > 0:
            csv_write.writerow([key,value])
print('FILE CREATED SUCCESSFULLY')
