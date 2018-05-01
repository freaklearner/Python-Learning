class Cat():

    def __init__(self,name,toy):
        self.name=name
        self.toy = toy

    def __repr__(self):
        return "Cat name is {}".format(self.name)

    def plays_with(self):
        print("{} plays with {}".format(self.name,self.toy))
