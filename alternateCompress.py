print("Enter data to compress: ")
data = input()
a_string = list(data)
data = ''
while len(a_string)>0:
    print(a_string)
    x = a_string[0]
    data += x + str(a_string.count(x))
    while a_string.count(x)>0:
        a_string.remove(x)
print(data)
