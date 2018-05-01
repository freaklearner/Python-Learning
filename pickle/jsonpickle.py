import json
from classes import Cat

c = Cat('charles','ball')

j = json.dumps(c.__dict__) 
print(j)
