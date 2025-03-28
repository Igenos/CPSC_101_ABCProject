# Game Abstract Base Class Project

## Overview

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

## Project Structure

### Board Representation

The ABC that is core to this project will define all the components absolutely required for a game with the following constraints:

- The game is played on a 2-dimensional plane.
  - All spaces within that plane are defined by the vector $(x,y) \in \mathbb{Z}$
  - The playable area will be a finite subset of the above.
  - Each vector may have more dimensions in order to store other values. For example:
    - Chess is played on an 8 x 8 grid with 2 color options for tiles / peices and 6 different peices might have their vector spaces defined as:
    - $(x, y, space\_color, piece)$ where 
      - $x, y \in \mathbb{Z}: 0 \leq x, y \leq 7$,
      - space_color $\in \mathbb{Z}:0\geq$ space_color $\geq1$,
      - and peice is $\in\mathbb{Z}:-6\geq$ piece $\geq6$ Negative indicating black peices and positive indicating white.

### Agents

- The game will have $\geq2$ agents.
- Each agent may be either a human player or an algorithm.
- Each agent will be an object that is passed the board state and returns their move.
- All agents have the same, or mirrored, win condition.

### Turn Flow

- Initial board state is set and first player is chosen.
- Play progresses in turns where one agent is active and no others can effect the board state.
- The game end condition will be checked for after the board state is updated with an agents move and before play passes for the next agent.

## Methods

### Game Logic Flow

Initial turn:

1. `start_game()`
2. `setup_board()`
3. `game_record()`
4. `choose_next_player()`
5. `player_move()`
6. `update_board_state()`
7. `check_win_condition()`
8. `progress_game()`

Subsequent Turns

1. `choose_next_player()`
2. `player_move()`
3. `update_board_state()`
4. `check_win_condition()`
5. `progress_game()`

### Method Deffinitions

1. `start_game(path to current game file) -> bool`
    - This function takes the return of the Initial Board State as an arg, creates a new Game Record and sets the first_move flag.
2. `setup_board() -> bool`
    - Creates a list of args to pass to game_record in order to create the game file.
    - returns true if no exceptions are raised.
3. `game_record(path to save dir, return of setup_board) -> path to current game file`
    - Creates a new save game file and verifies it's permissions are rw.
4. `choose_next_player(last_player: int) -> int`
    - A function that takes the last player as an arg and returns the next player, or returns the first player if the first_move flag is True.
5. `player_move(board_state) -> board_state`
    - A function that takes the current board state as an arg and returns a move. This contains all the logic or options that agent has available to them.
6. `update_board_state(board_state) -> board_state`
    - A function that takes a player move and the current board state as args, verifies their validity, then returns a new immutable board state object that stores all the vectors for the spaces and the move argument it was originally passed. It will have the turn number in it's name and that will be stored in the Game Record.
7. `check_win_condition(board_state) -> bool`
    - A function that checks the board state against the defined end conditions and returns either a player or False.
8. `progress_game(bool) -> None`
    - Chooses either to progress to the next turn or do something else at game end.

## Dependencies

- abc, a builtin python module. [source code](https://github.com/python/cpython/tree/3.13/Lib/abc.py)

## Resources

### Official Python 3.13.2 documentation

- [abc — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [collections.abc — Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html)

### Other usefull resources

- [Teclado - How to Write Cleaner Python Code Using Abstract Classes](https://blog.teclado.com/python-abc-abstract-base-classes/)
- [Abstract Base Classes in Python](https://earthly.dev/blog/abstract-base-classes-python/)
