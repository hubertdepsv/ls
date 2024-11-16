class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.owner = ''

class Shelter:
    def __init__(self):
        self.owners = []

    def adopt(self, adopter, pet):
        pet.owner = adopter
        adopter.nb_of_pets += 1
        adopter.pets.append(pet)
        if adopter not in self.owners:
            self.owners.append(adopter)

    def print_adoptions(self):
        for owner in self.owners:
            print(f"\n{owner.name} has adopted the following pets:")
            for pet in owner.pets:
                print(f"a {pet.species} named {pet.name}")
        print("\n")

class Owner:
    def __init__(self, name):
        self.name = name
        self.nb_of_pets = 0
        self.pets = []

    def number_of_pets(self):
        return self.nb_of_pets

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")

# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.