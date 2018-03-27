class MyClass:
    variable = "icon"

    def function(self):
        print("this is a message inside a class")


MyObject = MyClass()

print(MyObject.variable)

print(MyObject.function())

obj2 = MyClass()

obj2.variable = "screen icon"

print(MyObject.variable)
print(obj2.variable)


class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value=100.00

    def description(self):
        desc_str = "%s is a %s %s worth of $%0.2f" % (self.name,self.color,self.kind,self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertable"
car1.value=60000.00

car2 = Vehicle()
car2.name="Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00
print(car1.description())
print(car2.description())
