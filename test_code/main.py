from animalABC import Animal
from abc import ABC, abstractmethod

class dog(Animal):
    
    def __init__(self, name: str, food_type: str) -> object:
        self.name: str = name
        self.food_type: str = food_type

    @abstractmethod
    def eat(self):
        return(f"{self.name} ate the {self.food_type}")

    # @property
    # def name(self):
    #     return self.name()

    # @property
    # def food_type(self):
    #     return self.food_type

if __name__ == '__main__':
    
    # Setup our list of dogs using subclass __init__.
    dogs: list[dog] = [
        dog("Alice" , "meat") , 
        dog("Max" , "vegetarian feed") , 
        dog("Charlie" , "double meat portions") , 
        dog("Nicole" , "guten free feed") ]

    # Use adstract base method to feed the dogs.from animalABC import Animal
    for dog in dogs:
        print(dog.__feed__())

    for dog in dogs:
        print(dog.eat())