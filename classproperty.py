class Human:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        if age>0:
            self._age = age
        else:
            self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if value>0:
            self._age = value
        else:
            raise ValueError("age cannot be negative")

john = Human('john','rider',34)
#print(john.age)
john.age = -100
