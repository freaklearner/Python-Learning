class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def __repr__(self):
        return '{} is {}'.format(self.name,self.species)

class Cat(Animal):
    def __init__(self,name,breed,toy):
        super().__init__(name,species='Cat')
        self.breed = breed
        self.toy = toy

    def play(self):
        print("{} plays with {}".format(self.name,self.toy))

blue = Cat('joy','urban','string')
print(str(blue))

blue.play()
