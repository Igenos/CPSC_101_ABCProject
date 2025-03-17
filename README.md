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

A properly implemented ABC will not allow the user to implement an instance of the base class. In order to implement an instance of the ABC they must:

- Define a subclass of the ABC.
- Then define all properties and methods within the subclass. 
- At compilation, it will return an error if any of the requirements are not defined.
    - Properties required by the parent ABC are defined by the @properies decorator.
    - Methods required by the parent ABC simply need to be included.

## Structure for Grid_Game

The ABC that is core to this project will define all the components absolutely required for a game with the following constraints:

- The game is played on a 2-dimensional plane.
  - All spaces within that plane are defined by the vector $(x,y) \in \mathbb{Z}$
  - The playable area will be a finite subset of the above.
  - Each vector may have more dimensions in order to store other values. For example:
    - A game on an 8 x 8 grid with 2 color options for tiles / peices and 6 different peices might have their vector spaces defined as:
    - (x, y, space_color, piece) where $x,y\in\mathbb{Z}:0\geq x,y \geq 7$ , space_color is $\in \mathbb{Z}:0\geq$ val $\geq1$, and peice is $\in\mathbb{Z}:-6\geq$ piece $\geq6$.
- The game will have $\geq1$ agents that can effect the board state.
  - Each agent may be either a human player or an algorithm.
  - Play progresses in turns where one agent is active and no others can effect the board state.
  - Each agent will be an object that is passed the board state and returns their move.
  - All agents have the same, or mirrored, win condition.
- The game end condition will be checked for after the board state is updated with an agents move and before play passes for the next agent.

## Methods Required

1. **Game Record :** This ?file? will store all initial conditions, all board states passed to it, and all other variables that the current game uses.
2. **Initial Board State :** This will store all conditions required for the start of the game. It may also contain prompts from the user for any initial conditions defined as mutable.
3. **Start :** This function takes the return of the Initial Board State as an arg, creates a new Game Record and sets the first_move flag.
4. **Choose Next Player :** A function that takes the last player as an arg and returns the next player, or returns the first player if the first_move flag is True.
5. **Player Move :** A function that takes the current board state as an arg and returns a move. This contains all the logic or options that agent has available to them.
6. **Update Board State :** A function that takes a player move and the current board state as args, verifies their validity, then returns a new immutable board state object that stores all the vectors for the spaces and the move argument it was originally passed. It will have the turn number in it's name and that will be stored in the Game Record.
7. **Check for Gane End :** A function that checks the board state against the defined end conditions and returns either a player or False.
8. 

## Dependencies

- abc, a builtin python module. [source code](https://github.com/python/cpython/tree/3.13/Lib/abc.py)

## Resources

### Official Python 3.13.2 documentation

- [abc — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [collections.abc — Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html)

### Other usefull resources

- [Teclado - How to Write Cleaner Python Code Using Abstract Classes](https://blog.teclado.com/python-abc-abstract-base-classes/)
- [Abstract Base Classes in Python](https://earthly.dev/blog/abstract-base-classes-python/)
