def reducer(content):
    dic = {}
    for c in content:
        if c in dic:
            dic[c]+=1
            #dic[c] = int(dic[c])+1
        else:
            dic[c]=1
    return dic

    
