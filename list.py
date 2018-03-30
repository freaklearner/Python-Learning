import sys
sys.path.append(r'/usr/lib/python2.7/dist-packages/')
import numpy as nm

mylist = []

mylist.append("Hello")
mylist.append("World")
mylist.append("How")
mylist.append("you")
mylist.append("doing")
mylist.sort
str = ""
for x in mylist:
	str = str + x + " "

print(str)

fruits = ['Apple','Mango','Grapes']

print(fruits[0])
print(fruits[1])
print(fruits[2])


#check if list contains an item
if 'Orange' in fruits:
        print("It contains Apples")
else:
        print("It doesn't contains Apples")

#sum of the elements of the list

d = []


for x in range(2,6,2):
        d.append(x)

ar = nm.array(d)
print(ar.sum())
