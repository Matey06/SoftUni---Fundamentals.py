class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, specie, name):
        if specie == 'mammal':
            self.mammals.append(name)
        elif specie == 'fish':
            self.fishes.append(name)
        elif specie == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, specie):
        result = ''
        if specie == 'mammal':
            result += f'Mammals in {self.name}: {", ".join(self.mammals)}'
        elif specie == 'fish':
            result += f'Fishes in {self.name}: {", ".join(self.fishes)}'
        elif specie == 'bird':
            result += f'Birds in {self.name}: {", ".join(self.birds)}'

        result += f'\nTotal animals: {Zoo.__animals}'
        return result

zoo_name = input()
animals_num = int(input())

zoo = Zoo(zoo_name)

for current_animal in range(animals_num):
    species, name_ = input().split()
    zoo.add_animal(species, name_)

specie_ = input()

print(zoo.get_info(specie_))