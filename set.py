num = {1,2,3,4,5,5,5,5,5}
print(num)

# remove duplicates from the string using set but the order get changed
name = 'shubhssssshhhnnhhuubb'
rm_dup = set(name)
name = ''.join(rm_dup)
print(name)



# .add(item) method adds an item to the set
num.add(7)
print(num)

# remove(item) removes an item from the insert
num.remove(5)
print(num)

#remove(item) gives an error if item is not in the list. Alternative is discard(item) which remove an item and doesn't give an error if item is not in the a_list
num.discard(10) # this will not give an error even as 10 is not in the set num
num.discard(3) # this will remove the item 3 from the set
print(num)


# .copy() method creates a set with same elements as in original but both are different sets
num_copy = num.copy()
print(num_copy)
print(num_copy == num) # true because both have similar elements
print(num_copy is num) # false because both are different sets like objects in java

# set operations like union and intersections
math_club = {'rajat','abhishek','ani','aarti'}
sports_club = {'rajat','shub','riya','aarti'}
print("Math Club")
print(math_club)
print("Sports_Club")
print(sports_club)
print()
print("Union of math_club and sports_club")
print(math_club | sports_club)

print()
print("Intersection of math_club and sports_club")
print(math_club & sports_club)
