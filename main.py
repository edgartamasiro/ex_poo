class Dog:
    def __init__(self, race):
        self.race = race
        self.age = 10
        print('{} criado'.format(race))
    
    def get_old(self):
        self.age += 1
        return self.age

# herança (inheritance)
class Animal:
    def __init__(self):
        print('Animal criado')
    
    def quem_sou_eu(self):
        print('Eu sou um animal')
    
    def comer(self):
        print('Comendo')

class Cachorro(Animal):
    def quem_sou_eu(self):
        print('Eu sou um cachorro')

catiorro = Dog('Labrador')
doguinho = Dog('Huskie')
print(catiorro.age)
print(catiorro.race)
catiorro.get_old()
print(catiorro.age)
print(catiorro.race)
print(doguinho.age)
print(doguinho.race)

animal = Animal()
animal.quem_sou_eu()

dog = Cachorro()
dog.quem_sou_eu()




