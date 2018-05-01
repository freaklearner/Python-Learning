#Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first letter of each name in the list.
#I would use a list comprehension, though you could also loop over manually.

#Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.
#Another good candidate for a list comp.

list1 = ["Elie", "Tim", "Matt"]
list2 = [1,2,3,4,5,6]

ans1 = [s[0] for s in list1]
print(ans1)

ans2 = [s for s in list2 if s%2==0]
print(ans2)
