print("Enter string with duplicates enteries")
data = input()
a_string = list(data)
b_string = []
for x in a_string:
    if x not in b_string:
        b_string.append(x)

result_string = ''.join(b_string)
print(result_string)
