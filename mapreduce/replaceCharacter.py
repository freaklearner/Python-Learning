def replaceChar(fl,old,new):
    file = open(fl,'r+a')
    data = file.read()
    file.seek(0)
    data = data.replace(old,new)
    file.write(data)
    return
