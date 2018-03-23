name = "John"
age = 23

if name == "John" and age ==23:
	print("Your name is john and your age is 23")

if name == "John" or name == "Rick":
	print("Either you are John or Rick")


if name in ["John","Rick"]:
	print("Either you are John or Rick")

eng,maths,sci = 70,80,99
avg = (eng+maths+sci)/3
if avg>=90:
        print("A Grade")
elif avg>=80:
        print("B Grade")
elif avg>=70:
        print("C Grade")
elif avg>=60:
        print("D Grade")
else:
        print("D- Grade")

x = [1,2,3]
y = [1,2,3]

print(x==y)

print(x is y)
        
