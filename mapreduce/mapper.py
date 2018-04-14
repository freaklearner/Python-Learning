import re
def mapper(line,sep):
    if sep == ' ':        
        words = re.split('["().\s]|,|--',line)
    else:
        words = line.split(sep)
    return words
