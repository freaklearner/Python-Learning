import matplotlib.pyplot as ppt

population_age = [22,26,58,69,11,22,45,55,12,34,10,67,44,24,33,55,3,67,23,45,11,34,46,55,23,46,24,67,24,23,45,22,45,24,56,78,34,27,64,75,77,86,96,45]
bins = [0,10,20,30,40,50,60,70,80,90,100]
ppt.hist(population_age,bins,histtype='bar',rwidth=0.8)
ppt.title('ages of people in office')
ppt.legend()

ppt.show()
