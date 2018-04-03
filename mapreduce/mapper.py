def mapper(line,sep):
    if sep == ' ':
        words = line.split()    
    else:
        words = line.split(sep)    
    return words
