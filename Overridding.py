class Animal():
    def eating(self, meal: str) -> str:
        return f"Animal is eating {meal}"
    

class Bird(Animal):
    def eating(self, meal: str) -> str:
        return f"Bird is eating {meal}"
    

# Object 1
bird_obj: Bird = Bird()
print(bird_obj.eating("grains"))

# Object 2
animal_obj: Animal = Animal()
print(animal_obj.eating("grains"))

# Polymorphism Example
poly_obj: Animal = Bird()
print(poly_obj.eating("grains"))
