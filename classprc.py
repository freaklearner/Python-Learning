class user:
    activated_users = 0

    @classmethod
    def get_active_users(cls):
        return cls.activated_users

    @classmethod
    def from_string(cls,data_str):
        values = data_str.split(',')
        return cls(values[0],values[1],int(values[2]))

    def __repr__(self):
        return '{} {} is {}'.format(self.first,self.last,self.age)

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        user.activated_users +=1

    def full_name(self):
        return "{} {}".format(self.first,self.last)


    def initials(self):
        return "{}.{}".format(self.first[0],self.last[0])


user1 = user('Shubham','thakur',24)
user2 = user('Ani','thakur',22)
print(user.get_active_users())
print(user1.full_name())
print(user1.initials())
user3 = user('Shubham','thakur',24)
user4 = user('Ani','thakur',22)
print(user.get_active_users())

tom = user.from_string('tom,jones,24')
print(tom.first)
print(tom.last)

j = user('john','rider',25)
print(str(j))
