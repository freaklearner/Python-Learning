import mapper as m
import reducer as r

#lines = ["this is python class","hello this is shubham learning python","hi python is on","this is a python program for mapper and reducer"]
f1 = open("textfile.txt")
content = []
for w in f1.readlines():
    words = m.mapper(w,' ')
    content = content + words
f1.close()
    
data = r.reducer(content)
fl = open(r'keyValueFile.csv','w')
for k,v in data.items():
    print("%s : %d" % (k,v))
    data = str(k)+":"+str(v)+"\n"
    fl.write(data)
fl.close()

    
