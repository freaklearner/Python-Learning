def reducer(content):
    dic = {}
    for c in content:
        if c in dic:
            dic[c]+=1
            #dic[c] = int(dic[c])+1
        else:
            print(c)
            c = str(c)
            dic[c]=1
    return dic
