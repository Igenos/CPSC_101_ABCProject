from lib.Grid_GameABC import Grid_Game, Board_State
from abc import ABC, abstractmethod
import sqlite3
import datetime
import logging
import tkinter as tk
from pathlib import Path


class Move():
    def __init__(self, player: int, player_move: list[int]):
        """Represents a single move on the grid by a player."""
        self.player = player
        self.x_dim: int = player_move[0]
        self.y_dim: int = player_move[1]

    def __str__(self):
        return f"Player {self.player} chose to play ({self.x_dim}, {self.y_dim})"


class board_state(Board_State):
    """Contains all information required to describe the board state at a given turn."""

    def __init__(self, turn: int = 1, current_player: int = 1, moves_played: dict = None, player_count: int = 2, is_winner: bool = False):
        super().__init__()
        self.turn = turn
        self.player_count = player_count
        self.current_player = current_player
        self.is_winner = is_winner
        self.is_tie: bool = False
        self.board_vectors: dict = {} if moves_played is None else moves_played

    @property
    def position_map(self) -> dict:
        """Returns a mapping from (x, y) coordinates to player numbers."""
        return {
            (move.x_dim, move.y_dim): move.player for move in self.board_vectors.values()
        }

    def __str__(self):
        return '\n'.join([f"{index}, {move}" for index, move in self.board_vectors.items()])


class tic_tac_toe(Grid_Game):
    """Implements the Tic-Tac-Toe game logic and interface using tkinter."""

    def __init__(self):
        super().__init__()

        # Any flags required.
        self.is_first_turn: bool = True
        self.is_winner: bool = False

        # Find out where we are.
        self.current_directory: Path = Path(__file__).parent.absolute()
        self.save_directory: Path = self.current_directory / 'current_game.db'

        # SQLite setup
        self.connection = sqlite3.connect(self.save_directory)
        self.cursor = self.connection.cursor()
        self.table_name: str = f"Game({time})"

        # Define board boundaries and create current_board object.
        self.x_max = 3
        self.y_max = 3
        self.win_length = 3
        self.current_board: board_state = board_state()

        # Create interface objects using tkinter.
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")

        self.buttons = []
        for y_grid in range(self.y_max):
            row_of_buttons = []
            for x_grid in range(self.x_max):
                button = tk.Button(
                    self.root, text="", width=10, height=5,
                    command=lambda x=x_grid, y=y_grid: self.game_loop_onclick(x, y)
                )
                button.grid(row=y_grid, column=x_grid)
                row_of_buttons.append(button)
            self.buttons.append(row_of_buttons)

        # Start logger
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename='ttt_game.log', encoding='utf-8', level=logging.INFO)
        self.logger.info(f"{datetime.datetime.now()} - New game started")

        # Start GUI mainloop.
        self.root.mainloop()

    def game_loop_onclick(self, x_dim, y_dim) -> None:
        """Processes a player's click on the board and progresses the game."""
        
        move = self.player_move(x_dim, y_dim)
        updated_board = self.update_board_state(self.current_board, move)
        updated_board = self.check_win_condition(updated_board)
        self.game_record(updated_board)
        self.current_board = self.choose_next_player(updated_board)
        print(self.current_board)

    def game_record(self, board_update: board_state) -> bool:
        """Stub function to handle recording the board state."""
        return True

    def choose_next_player(self, current_board: board_state) -> board_state:
        """Determines the next player and returns a new board state."""
        
        if current_board.current_player < current_board.player_count:
            return board_state(
                turn=current_board.turn + 1,
                current_player=current_board.current_player + 1,
                moves_played=current_board.board_vectors.copy()
            )
        else:
            return board_state(
                turn=current_board.turn + 1,
                current_player=1,
                moves_played=current_board.board_vectors.copy()
            )

    def player_move(self, x_dim, y_dim) -> Move:
        """Creates a Move object from the player's input and updates the button text."""

        self.buttons[y_dim][x_dim]["state"] = "disabled"
        self.buttons[y_dim][x_dim]["text"] = "X" if self.current_board.current_player == 1 else "O"
        return Move(self.current_board.current_player, [x_dim, y_dim])

    def update_board_state(self, old_board: board_state, played_move: Move) -> board_state:
        """Returns a new board state object that includes the latest move."""

        new_board_vectors: dict = old_board.board_vectors.copy()
        new_board_vectors[f"Turn {old_board.turn}"] = played_move
        return board_state(
            turn=old_board.turn,
            current_player=old_board.current_player,
            moves_played=new_board_vectors
        )

    def check_win_condition(self, current_board: board_state) -> board_state:
        """Checks the board for a win or tie condition and returns the updated state."""

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for move in current_board.position_map.keys():
            player = current_board.position_map[move]
            for dx, dy in directions:
                length = 1

                pos_direction = (move[0] + dx, move[1] + dy)
                while pos_direction in current_board.position_map and current_board.position_map[pos_direction] == player:
                    length += 1
                    pos_direction = (pos_direction[0] + dx, pos_direction[1] + dy)

                neg_direction = (move[0] - dx, move[1] - dy)
                while neg_direction in current_board.position_map and current_board.position_map[neg_direction] == player:
                    length += 1
                    neg_direction = (neg_direction[0] - dx, neg_direction[1] - dy)

                if length >= self.win_length:
                    current_board.is_winner = True

        # Check for tie after all win conditions are verified
        if not current_board.is_winner and len(current_board.position_map) == self.x_max * self.y_max:
            for y_dim in range(3):
                for x_dim in range(3):
                    self.buttons[y_dim][x_dim]["state"] = "disabled"
            game_end_board = current_board
            game_end_board.is_tie = True
            print("It's a tie!")
            return game_end_board

        if current_board.is_winner:
            for y_dim in range(3):
                for x_dim in range(3):
                    self.buttons[y_dim][x_dim]["state"] = "disabled"
            game_end_board = current_board
            game_end_board.is_winner = True
            print(f"winner is player {current_board.current_player}")
            return game_end_board

        return current_board


if __name__ == "__main__":
    time = datetime.datetime.now()
    test_game = tic_tac_toe()
    print(test_game.is_first_turn, test_game.current_directory, test_game.save_directory, test_game.connection, test_game.table_name)
    print("It worked.")
