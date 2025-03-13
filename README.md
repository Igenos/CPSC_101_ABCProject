# Game Abstract Base Class Project

A project focussed on developing an Abstract Base Class (abc) in python. An ABC is annalogous to a template for an object. There are two main reasons why one would implement an ABC.

1. To streamline the creation of various instances of similar objects. For example, if you had many instances of a animal object and wanted them all to the properties "name" & "food_type" with the method "feed".

'''python
from animalABC import Animal
class Animal(ABC):
    def __feed__(self, daily_feedings: int = 3) -> str:
        return(f"{self.name} must be fed {self.food_type} .")
dogs: list[dog] = [
   dog("Alice" , "meat") , 
   dog("Max" , "vegetarian feed") , 
   dog("Charlie" , "double meat portions") , 
   dog("Nicole" , "guten free feed") ]

for dog in dogs:
    print(dog.__feed__())
'''

2. As a project management tool to guide the creation of a complex object. It can ensure the subclass created can be implemented safely into a larger body of code without the team building it requiring full knowledge of it's implementation.

I will develop an abc called Grid_Game

A properly implemented ABC will not allow the uer to implement an instance of the base class, they must implement a subclass and define all properties and methods within the subclass. An ABC can define properties and methods that the subclass must define in order to create the class. We can either fully define them in the ABC or leave them blank for the user to define.

- Properties are defined by the @properies decorator.
- Methods are defined with the @

## Objectives

1. To display a functional understanding of object oriented programming and abstract base classes in Python.
2. To show an understanding of python best coding practices.

## Dependencies

- ABC, a builtin python module. [source code](https://github.com/python/cpython/tree/3.13/Lib/abc.py)

## Resources

### Official Python 3.13.2 documentation

- [abc — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [collections.abc — Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html)

### Other usefull resources

- [Teclado - How to Write Cleaner Python Code Using Abstract Classes](https://blog.teclado.com/python-abc-abstract-base-classes/)
- [Abstract Base Classes in Python](https://earthly.dev/blog/abstract-base-classes-python/)
