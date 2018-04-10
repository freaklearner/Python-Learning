import os
from os import path
import extractwordsfile as ewf
import reducer as rd
import mapper as m
files_path =  path.join(os.getcwd(),'filescollection')  #str(os.getcwd()) + '/filescollection'
print(files_path)
files = [f for f in os.listdir(files_path) if path.isfile(path.join(files_path,f))]
content = []
for fl in files:
    content.extend(ewf.extractwordsfromfile(path.join(files_path,fl)))
dic = rd.reducer(content)
fl = open(path.join(os.getcwd(),'wordscount.txt'),'w')
for key in dic.keys():
    if len(key) > 0:
        data = str(key)+'='+str(dic.get(key))+'\n'
        fl.write(data)
fl.close()
print('FILE CREATED SUCCESSFULLY')
