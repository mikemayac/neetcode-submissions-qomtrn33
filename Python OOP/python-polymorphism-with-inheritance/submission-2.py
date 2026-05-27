class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self) -> None:
        print("Animal is making a sound")


# TODO: Create the Dog and Cat classes with make_sound method
class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says: Meow!")

# TODO: Create a common interface that takes any object of type Animal (or its subclasses) and calls their make_sound method
def trigger_animal_sound(animal_instance: Animal) -> None:
    animal_instance.make_sound()

# Do not change the code below
animal = Animal("Rabbit")
trigger_animal_sound(animal)

animal = Dog("Buddy")
trigger_animal_sound(animal)

animal = Cat("Whiskers")
trigger_animal_sound(animal)
