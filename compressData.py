print("Enter a string")
a_string = input()
#print(a_string)
data = ''
index = 0
while index<len(a_string) and not a_string.isdigit():
    x = a_string[index]
    if x is not '0':
        data += x + str(a_string.count(x))
        a_string = a_string.replace(x,'0')
    index+=1
print(data)
