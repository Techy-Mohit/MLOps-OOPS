# Simple inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")
    
# Derived class
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        super().speak() # call the base class method
        print(f"{self.name} barks. It is a {self.breed}.")

# create an instance of Animal
# animal = Animal("Generic Animal")
# animal.speak()

# create an instance of Dog
dog = Dog("Buddy","Golden Retriever")
dog.speak()