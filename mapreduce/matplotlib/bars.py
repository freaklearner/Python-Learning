import matplotlib.pyplot as ppt

x = [1,5,8]
y = [10,20,5]

x2 = [2,6,10]
y2 = [10,18,7]
ppt.bar(x,y,label='Trump',color='r')
ppt.bar(x2,y2,label='Modi',color='pink' )
ppt.legend()
ppt.title('tweets')
ppt.show()
