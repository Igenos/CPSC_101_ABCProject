# Game Abstract Base Class Project

A project focussed on developing an Abstract Base Class (abc) in python called Grid_Game. It will primarilly focus around the correct implementation of a Base Class that will have all the abstract methods required for any game that is played on a grid with multiple players (either human or algorithmic).

## Objectives

1. To display a functional understanding of object oriented programming and abstract base classes in Python.
2. To show an understanding of python best coding practices.

## What is an Abstract Base Class?

An ABC is annalogous to a template for an object. It is by deffinition impossible to implement an instance of the Abstract Base Class, it's function is to create a framework for the creation of child classes. These are some examples of why one would implement an ABC.

1. To streamline the creation of various instances of similar objects. For example, if you had a zoo with many diffent animals and need to make many instances of a animal object and wanted them all to have the same methods and properties so that they can be implemented repeatably.

2. As a project management tool to guide the creation of a complex object. It can ensure the subclass created can be implemented safely into a larger body of code without the team building it requiring full knowledge of it's implementation.

3. If a bank had a specific way it wanted online transactions processed and logged. An ABC would be created for transactions, and the different types of transactions could be derived from that. For example: mastercard(Transaction), visa(Transaction), etc...

A properly implemented ABC will not allow the uer to implement an instance of the base class. In order to implement an instance of the ABC they must:

- Define a subclass of the ABC.
- Then define all properties and methods within the subclass. 
- At compilation, it will return an error if any of the requirements are not defined.
    - Properties required by the parent ABC are defined by the @properies decorator.
    - Methods required by the parent ABC simply need to be included.

## Dependencies

- abc, a builtin python module. [source code](https://github.com/python/cpython/tree/3.13/Lib/abc.py)

## Resources

### Official Python 3.13.2 documentation

- [abc — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [collections.abc — Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html)

### Other usefull resources

- [Teclado - How to Write Cleaner Python Code Using Abstract Classes](https://blog.teclado.com/python-abc-abstract-base-classes/)
- [Abstract Base Classes in Python](https://earthly.dev/blog/abstract-base-classes-python/)
