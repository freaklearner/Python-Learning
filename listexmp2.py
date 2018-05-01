n1 = [1,2,3,4]
n2 = [3,4,5,6]
# intersection of n1 & n2
ans1 = [s for s in n1 if s in n2]
print(ans1)


n_list = ["Elie", "Tim", "Matt"]
#ans2 = [s.lower() for s in [r[::-1] for r in n_list]]
ans2 =[s[::-1].lower() for s in n_list]
print(ans2)
