phonebook = {}
phonebook["shub"] = 9999999999
phonebook["abhi"] = 8888888888
phonebook["Ani"] = 9898989898
phonebook["rjt"] = 7777889987
phonebook["rjt"] = 7777889987
print(phonebook)


phonebook["varun"] = 8768769800
phonebook.pop("abhi")

if "varun" in phonebook:
    print("%s add to phonebook"%("varun"))

if "abhi" not in phonebook:
    print("%s has been poped"%("abhi"))





fruit_color = {
    "Apple" : "red",
    "Mango" : "yellow",
    "Orange" : "orange",
    "banana" : "yellow"
    }

for f,c in fruit_color.items():
    print("%s is of %s color"%(f,c))

print(fruit_color)
fruit_color.pop("banana")
print(sorted(fruit_color))

del fruit_color["Mango"]
print(sorted(fruit_color))

#2D

tables = {}
tables["two"]=[]
for x in range(2,21,2):
    tables["two"].append(x)

print(tables)
