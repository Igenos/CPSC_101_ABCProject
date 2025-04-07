from abc import ABC, abstractmethod

class Board_State(ABC):
    pass

class Grid_Game(ABC):
    """This ABC is to be used to create a game played on a grid. It inherits from ABC.
    
    required methods:
    1. start_game(path to current game file) -> bool
        - This function takes the return of the Initial Board State as an arg, creates a new Game Record and sets the first_move flag.
    2. setup_board() -> bool
        - Creates a list of args to pass to game_record in order to create the game file.
        - returns true if no exceptions are raised.
    3. game_record(path to save dir, return of setup_board) -> path to current game file
        - Creates a new save game file and verifies it's permissions are rw.
    4. choose_next_player(last_player: int) -> int
        - A function that takes the last player as an arg and returns the next player, or returns the first player if the first_move flag is True.
    5. player_move(board_state) -> board_state
        - A function that takes the current board state as an arg and returns a move. This contains all the logic or options that agent has available to them.
    6. update_board_state(board_state) -> board_state
        - A function that takes a player move and the current board state as args, verifies their validity, then returns a new immutable board state object that stores all the vectors for the spaces and the move argument it was originally passed. It will have the turn number in it's name and that will be stored in the Game Record.
    7. check_win_condition(board_state) -> bool
        - A function that checks the board state against the defined end conditions and returns either a player or False.
    8. progress_game(bool) -> None
        - Chooses either to progress to the next turn or do something else at game end.
    
    """

    @abstractmethod
    def game_loop_onclick(self) -> bool:
        """This function takes the return of the Initial Board State as an arg, creates a new Game Record and sets the first_move flag."""
        pass

    # @abstractmethod
    # def setup_board(self) -> list[tuple]:
    #     """Define all the values that will be stored in order to keep track of the game as at progresses.
    #     Create the empty table and then create the list of first values toi pass to game_record.
    #        These will be in pairs with column headers first, then the first value."""
    #     pass

    @abstractmethod
    def game_record(self):
        """Whenever this function is called, it adds a new row to the game record"""
        pass

    @abstractmethod
    def choose_next_player(self, last_player: int) -> int:
        """A function that takes the last player as an arg and returns the next player, or returns the first player if the first_move flag is True."""

    @abstractmethod
    def player_move(self, current_board: Board_State) -> Board_State:
        """A function that takes the current board state as an arg and returns a move. This contains all the logic or options that agent has available to them."""
        pass

    @abstractmethod
    def update_board_state(self, player_move: Board_State) -> Board_State:
        """A function that takes a player move and the current board state as args, verifies their validity, then returns a new immutable board state object that stores all the vectors for the spaces and the move argument it was originally passed. It will have the turn number in it's name and that will be stored in the Game Record."""
        pass

    @abstractmethod
    def check_win_condition(self, current_board: Board_State) -> bool:
        """A function that checks the board state against the defined end conditions and returns either a player or False."""
        pass

    # @abstractmethod
    # def progress_game(self, bool) -> None:
    #     """Chooses either to progress to the next turn or do something else at game end."""
    #     pass