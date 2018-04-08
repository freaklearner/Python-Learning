# removing duplicates using set() function
print('Enter a string with duplicates characters:')
name = input()
rm_dup = set(name)
name = ''.join(rm_dup)
print(name)
