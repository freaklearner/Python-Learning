class Animal:
    cool = True
    def make_sound(self,sound):
        print(sound)

class Cat(Animal):
    pass


blue = Cat()
blue.make_sound("Meaow")
print(Cat.cool)

print(isinstance(blue,Cat))
print(isinstance(blue,Animal))
