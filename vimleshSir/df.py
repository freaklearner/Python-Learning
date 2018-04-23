a =[1,2,3]
b =['1a','2v','3c']
import pandas as p

c= [a,b]
df = p.DataFrame(data=c)


print(df[0])

df = p.DataFrame(a,columns=['id'])

print(df['id'])




                            







