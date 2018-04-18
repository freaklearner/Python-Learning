import matplotlib.pyplot as ppt

x = [1,3,5]
y = [5,7,4]

x2 = [1,3,5]
y2 = [2,4,1]
ppt.plot(x,y,label = 'first line')
ppt.plot(x2,y2,label = 'Second Line')
ppt.xlabel('X values')
ppt.ylabel('Y values')
ppt.title('line graph\n check it out')
ppt.legend()
ppt.show()
