from abc import ABC, abstractmethod

class Move():
    def __init__(self, player: int, player_move: list[int], piece: tuple = None):
        """Represents a single move made by a player on the grid.
        
        Args:
            player (int): ID of the player making the move.
            player_move (list[int]): [x, y] coordinates of the move.
            piece (tuple, optional): Additional piece data (e.g., name, ID).
        """

        
        # Who made the move.
        self.player = player
        
        # Where did they move to.
        self.x_dim: int = player_move[0]
        self.y_dim: int = player_move[1]
                
        # What piece did they move. Str  as name of piece, value as piece ID.
        self.piece: tuple = piece
        

    def __str__(self) -> str:
        if self.piece is not None:
            return f"Player {self.player} moved {self.piece[0]} to ({self.x_dim}, {self.y_dim})"
        else:
            return f"Player {self.player} chose to play ({self.x_dim}, {self.y_dim})"

class Board_State(ABC):
    """Base class to describe the state of the game board at any point in time.
    
    Stores turn information, current player, move history, win/tie flags,
    and optional extra metadata passed via kwargs.
    """

    def __init__(self, turn: int = 1, current_player: int = 1, moves_played: dict = None, player_count: int = 2, is_winner: bool = False, *kwargs):
        super().__init__()
        self.turn = turn
        self.player_count = player_count
        self.current_player = current_player
        self.is_winner = is_winner
        self.is_tie: bool = False
        self.board_vectors: dict = {} if moves_played is None else moves_played

        # Catch-all for anything game-specific
        self.extra_state = kwargs

    @property
    def position_map(self) -> dict:
        """Returns a dictionary mapping (x, y) tuples to the player number.

        Useful for quick lookup of current player positions on the grid.
        """

        return {
            (move.x_dim, move.y_dim): move.player for move in self.board_vectors.values()
        }

    def __str__(self):
        return '\n'.join([f"{index}, {move}" for index, move in self.board_vectors.items()])

class Grid_Game(ABC):
    """Abstract base class for implementing any grid-based game.

    Defines the core interface for gameplay and state progression.
    Subclasses must implement methods for handling moves, board updates,
    win conditions, and data recording.
    """

    @abstractmethod
    def game_loop_onclick(self) -> bool:
        """Handles a single game loop cycle triggered by user interaction.

        Called when a grid button is clicked or a move is initiated.
        Should handle move creation, board update, win/tie check, and progression.
        """
        pass

    @abstractmethod
    def game_record(self):
        """Adds a new entry to the game record (e.g., a database, log, or in-memory list).

        Called after each move to persist or display game state.
        """

    def choose_next_player(self, current_board: Board_State) -> Board_State:
        """Calculates and returns the next player's turn.

        If current player < player count, increment player.
        Otherwise, reset to player 1.
        """

        if current_board.current_player < current_board.player_count:
            current_board.turn += 1
            current_board.current_player += 1
            return current_board
        else:
            current_board.turn += 1
            current_board.current_player = 1
            return current_board
        
    @abstractmethod
    def player_move(self, x_dim, y_dim, piece: tuple = None) -> Move:
        """Generates a Move object based on player input.

        Args:
            x_dim (int): X coordinate of the move.
            y_dim (int): Y coordinate of the move.
            piece (tuple, optional): Optional data for custom pieces (e.g., chess).

        Returns:
            Move: The move object for this turn.
        """
        pass

    @abstractmethod
    def update_board_state(self, old_board: Board_State, played_move: Move) -> Board_State:
        """Updates the board state with a new move and returns a new immutable state.

        Args:
            old_board (Board_State): Current board state.
            played_move (Move): Move to apply.

        Returns:
            Board_State: Updated state with the move applied.
        """
        pass

    @abstractmethod
    def check_win_condition(self, current_board: Board_State) -> Board_State:
        """Checks whether the current board meets win or tie conditions.

        Args:
            current_board (Board_State): Current game state.

        Returns:
            Board_State: Updated board with `is_winner` or `is_tie` flags set.
        """
        pass