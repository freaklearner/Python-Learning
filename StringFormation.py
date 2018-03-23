name = "xyz"
age = 21
print("%s is %d years old" % (name,age))

astring = "hello world"
print("length of 'hello World!' %d " % len("hello World!"))


print("Index of 'o' %d" % astring.index('o'))


print("Count 'l' %d" % astring.count('l'))


print(astring[3:7])


print(astring[3:7:2])


print(astring[::-1])


print(astring.upper())


print(astring.lower())

splitstring = astring.split(" ")

for x in splitstring:
	print(x)



