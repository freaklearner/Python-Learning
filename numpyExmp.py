height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import sys
sys.path.append(r'cd /usr/lib/python2.7/dist-packages')
import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(np_weight)

print(type(np_height))

#Calculate bmi
bmi = np_weight/np_height ** 2

print(bmi)

#Subsetting

print(bmi[bmi < 25])

print(bmi)
