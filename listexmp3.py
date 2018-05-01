#numbers between 1 and 100(including 100) that are divisable by 12
ans = [s for s in list(range(1,101)) if s%12==0]
print(ans)
