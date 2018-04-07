from __future__ import print_function
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

fruits = ['Apple','Mango','Grapes','Pineapple','Guava','Pomegranate','Banana']

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

#list with range
data = list(range(1,100))
print(data)


#indexing in mylist
for x in range(0,len(fruits)):
	print(fruits[x])

#backward indexing
for x in range(-1,len(fruits)-(len(fruits)*2)-1,-1):
	print(fruits[x])
		#or
for x in range(len(fruits)-1,-1,-1):
	print(fruits[x])
#	.extend(): extend adds more than one element in the list. it takes list of elements as an argument and append all that element into the list it call upon

data = ['carrot','potato','onion']
fruits.extend(data)
print(fruits)

# .insert()
data.insert(2,'cabage')
print(data)

# .clear(), it clears app the item from the list. But it doesn't work in python2
#data.clear()
#print(data)
first_list = list(range(1,5))
print(first_list)
last_item = first_list.pop()
print(last_item)
first_list.pop(1)
print(first_list)

# .remove() function, removes the passed argument from the list

name=['shub','ani','laksh','riya','rajat','rohan','rajat','abhi']
print('names: ',end='')
print(name)
name.remove('ani')
print('names: ',end='')
print(name)

#.index(number,start,end), index() gives the index number of the specified elements
number = [1,2,3,4,5,5,6,6,7,5,8,9,10]
print(number)
print("index of 3: %d"%number.index(3))
print("index of 5: %d"%number.index(5))
print("index of 5 after index-4: %d"%number.index(5,5))

#.count(num), how many times num appears in the list
print("5 appears in the list: %d" % number.count(5))
print("6 appears in the list: %d" % number.count(6))


#.reverse(), reverse the original first_list
print(number)
number.reverse()
print("Reverse: ")
print(number)
number.sort();
print(number)

a_string = ', '.join(name)
print(a_string)
