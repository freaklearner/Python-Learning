import pickle
from classes import Cat

with open('files/pets.pickle','rb') as file:
    data = pickle.load(file)
    print(data)
    data.plays_with()
