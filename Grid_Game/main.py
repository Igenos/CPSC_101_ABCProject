
from abc import ABC, abstractmethod
from lib.Grid_GameABC import Grid_Game, Board_State, Move

import sqlite3
import datetime
import logging
import tkinter as tk
from pathlib import Path

class TTT_Board(Board_State):
    def __init__(self, turn = 1, current_player = 1, moves_played = None, player_count = 2, is_winner = False):
        super().__init__(turn, current_player, moves_played, player_count, is_winner)

class tic_tac_toe(Grid_Game):
    """Implements the Tic-Tac-Toe game logic and interface using tkinter."""

    def __init__(self):
        super().__init__()

        # Find out where we are.
        self.current_directory: Path = Path(__file__).parent.absolute()
        self.save_directory: Path = self.current_directory / 'current_game.db'

        # SQLite setup
        self.connection = sqlite3.connect(self.save_directory)
        self.cursor = self.connection.cursor()
        self.table_name: str = f"Game({time})"

        # Define board boundaries and create current_board object. 
        # These vairables drive all the logic, so if you want to play a 10 x 10 game of TTT, you can.
        self.x_max = 3
        self.y_max = 3
        self.win_length = 3
        self.current_board: TTT_Board = TTT_Board()

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
        
        move = self.player_move(x_dim, y_dim)
        updated_board = self.update_board_state(self.current_board, move)
        updated_board = self.check_win_condition(updated_board)
        self.game_record(updated_board)
        self.current_board = self.choose_next_player(updated_board)
        print(self.current_board)

    def game_record(self, board_update: TTT_Board) -> bool:
        return True

    def player_move(self, x_dim, y_dim, piece: tuple = None) -> Move:

        self.buttons[y_dim][x_dim]["state"] = "disabled"
        self.buttons[y_dim][x_dim]["text"] = "X" if self.current_board.current_player == 1 else "O"
        
        return Move(self.current_board.current_player, [x_dim, y_dim])

    def update_board_state(self, old_board: TTT_Board, played_move: Move) -> TTT_Board:
        
        new_board_vectors: dict = old_board.board_vectors.copy()
        new_board_vectors[f"Turn {old_board.turn}"] = played_move
        return TTT_Board(
            turn=old_board.turn,
            current_player=old_board.current_player,
            moves_played=new_board_vectors
        )

    def check_win_condition(self, current_board: TTT_Board) -> TTT_Board:
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

        # Check for tie after all win conditions are verified, if all spaces are filled and there's no winner, that's a tie.
        if not current_board.is_winner and len(current_board.position_map) == self.x_max * self.y_max:
            for y_dim in range(3):
                for x_dim in range(3):
                    self.buttons[y_dim][x_dim]["state"] = "disabled"
            game_end_board = current_board
            game_end_board.is_tie = True
            print("It's a tie!")
            return game_end_board

        # Check for winner after all win conditions and  are verified
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
    logging.info(f"{datetime.datetime.now()} - Game executed successfully.")
