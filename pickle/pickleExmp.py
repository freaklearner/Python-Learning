import pickle
from classes import Cat



lily = Cat('lily','string')

with open('files/pets.pickle','wb') as file:
    pickle.dump(lily,file)
