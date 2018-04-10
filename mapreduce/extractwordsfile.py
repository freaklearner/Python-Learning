import mapper as m

def extractwordsfromfile(fl):
    fl = open(fl)
    content = []
    for line in fl.readlines():
        words = m.mapper(line,' ')
        content.extend(words)
    fl.close()
    return content
