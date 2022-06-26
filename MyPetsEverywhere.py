class Pet():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# New Cat


class Morty(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# list of cats
my_cats = [Simon('Simon', 2), Sally('Sally', 3), Morty('Morty', 5)]

# Instantiate pet class
my_pets = Pet(my_cats)

# Output of all cats walking
my_pets.walk()
