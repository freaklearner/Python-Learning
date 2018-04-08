num  = [1,2,3]
print(num)

square_num = [x**2 for x in num]
print(square_num)

cube_num = [x**3 for x in num]
print(cube_num)

name = 'lakshya'
print([x.upper() for x in name])

friends = ['rajat','abhishek','anuj','varun']
friends = [friend[0].upper() for friend in friends]
print(friends)


# convert number list into string
string_list = [str(x) for x in num]
print(string_list)
print(''.join(string_list))

number = list(range(1,20))
print(number)
even = [num for num in number if num % 2 == 0]
odd = [num for num in number if num % 2 != 0]
print(even)
print(odd)

a_list  = [num*2 if num%2==0 else num/2 for num in number]
print(a_list)

with_vowels = 'this is so much fun!'
print(with_vowels)
without_vowels = ''.join([char for char in with_vowels if char not in 'aeiou'])
print(without_vowels)
